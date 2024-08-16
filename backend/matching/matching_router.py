from fastapi import APIRouter, HTTPException, Depends, Security
from database import get_matchdb, get_userdb, get_historydb
from sqlalchemy.orm import Session
from models import Matching as MatchingModel, Lobby as LobbyModel, LobbyUser as LobbyUserModel, User as UserModel
from matching.matching_schema import MatchingCreate, MatchingResponse, LobbyResponse, LobbyListResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from matching.matching_crud import decode_jwt
from history.history_schema import HistoryCreate
from history.history_router import create_history
from datetime import datetime
from typing import List
security = HTTPBearer()
router = APIRouter(prefix="/matching")

def get_current_user(credentials: HTTPAuthorizationCredentials, db: Session):
    token = credentials.credentials
    payload = decode_jwt(token)
    user_id = payload.get("sub")

    user = db.query(UserModel).filter(UserModel.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/create", response_model=MatchingResponse)
def create_matching(
    matching: MatchingCreate,
    credentials: HTTPAuthorizationCredentials = Security(security),
    user_db: Session = Depends(get_userdb),
    match_db: Session = Depends(get_matchdb)
):
    user = get_current_user(credentials, user_db)

    db_matching = MatchingModel(
        matching_type=matching.matching_type,
        boarding_time=matching.boarding_time,
        depart=matching.depart,
        dest=matching.dest,
        max_member=matching.max_member,
        current_member=1,
        created_by=user.user_id,  
        mate=str(user.user_id)  
    )
    match_db.add(db_matching)
    match_db.commit()
    match_db.refresh(db_matching)

    # Lobby 생성
    db_lobby = LobbyModel(
        depart=matching.depart,
        dest=matching.dest,
        boarding_time=matching.boarding_time,
        max_member=matching.max_member,
        current_member=1,
        matching_id=db_matching.id,
        created_by=user.user_id  
    )
    match_db.add(db_lobby)
    match_db.commit()
    match_db.refresh(db_lobby)

    # 유저를 생성된 대기실에 추가
    lobby_user = LobbyUserModel(user_id=user.user_id, lobby_id=db_lobby.id)
    match_db.add(lobby_user)
    match_db.commit()
    match_db.refresh(lobby_user)

    return db_matching


@router.post("/lobbies/{lobby_id}/join", response_model=LobbyResponse)
def join_lobby(
    lobby_id: int,
    credentials: HTTPAuthorizationCredentials = Security(security),
    user_db: Session = Depends(get_userdb),
    match_db: Session = Depends(get_matchdb)
):
    user = get_current_user(credentials, user_db)

    existing_lobby_user = match_db.query(LobbyUserModel).filter(LobbyUserModel.user_id == user.user_id).first()
    if existing_lobby_user is not None:
        raise HTTPException(status_code=400, detail="유저가 이미 다른 대기실에 존재합니다")

    lobby = match_db.query(LobbyModel).filter(LobbyModel.id == lobby_id).first()
    if not lobby:
        raise HTTPException(status_code=404, detail="대기실을 찾을 수 없음")

    if lobby.current_member >= lobby.max_member:
        raise HTTPException(status_code=400, detail="대기실이 인원이 가득 찼습니다.")

    # LobbyUser 생성
    lobby_user = LobbyUserModel(lobby_id=lobby_id, user_id=user.user_id)
    lobby.current_member += 1
    match_db.add(lobby_user)
    match_db.commit()
    match_db.refresh(lobby_user)

    # Lobby 업데이트
    match_db.refresh(lobby)

    return lobby

@router.post("/lobbies/{lobby_id}/leave", response_model=LobbyResponse)
def leave_lobby(
    lobby_id: int,
    credentials: HTTPAuthorizationCredentials = Security(security),
    user_db: Session = Depends(get_userdb),
    match_db: Session = Depends(get_matchdb)
):
    user = get_current_user(credentials, user_db)

    lobby_user = match_db.query(LobbyUserModel).filter(LobbyUserModel.user_id == user.user_id, LobbyUserModel.lobby_id == lobby_id).first()
    if not lobby_user:
        raise HTTPException(status_code=404, detail="해당 유저는 대기실에 들어가 있지 않습니다.")

    lobby = match_db.query(LobbyModel).filter(LobbyModel.id == lobby_id).first()
    if not lobby:
        raise HTTPException(status_code=404, detail="대기실을 찾을 수 없음")

    # LobbyUser 삭제
    match_db.delete(lobby_user)
    lobby.current_member -= 1
    match_db.commit()
    match_db.refresh(lobby)

    return lobby

@router.get("/lobbies/{matching_type}/", response_model=List[LobbyResponse])
def list_lobbies_by_matching_type(matching_type: int, match_db: Session = Depends(get_matchdb)):
    # 주어진 matching_type에 해당하는 매칭들을 찾습니다.
    matchings = match_db.query(MatchingModel).filter(MatchingModel.matching_type == matching_type).all()

    if not matchings:
        raise HTTPException(status_code=404, detail="해당 매칭에 관련된 대기실이 존재하지 않습니다.")

    # 매칭들에 연결된 로비들을 수집합니다.
    lobbies = []
    for matching in matchings:
        matching_lobbies = match_db.query(LobbyModel).filter(LobbyModel.matching_id == matching.id).all()
        for lobby in matching_lobbies:
            lobbies.append(LobbyResponse(
                id=lobby.id,
                depart=lobby.depart,
                dest=lobby.dest,
                max_member=lobby.max_member,
                current_member=lobby.current_member,
                boarding_time=lobby.boarding_time,
                created_by=lobby.created_by
            ))

    # 수집한 로비 리스트를 반환합니다.
    return lobbies

@router.post("/lobbies/{lobby_id}/complete", response_model=dict)
def complete_lobby(
    lobby_id: int,
    credentials: HTTPAuthorizationCredentials = Security(security),
    user_db: Session = Depends(get_userdb),
    match_db: Session = Depends(get_matchdb)
):
    user = get_current_user(credentials, user_db)

    # 대기실 정보 가져오기
    lobby = match_db.query(LobbyModel).filter(LobbyModel.id == lobby_id).first()
    if not lobby:
        raise HTTPException(status_code=404, detail="대기실을 찾을 수 없음")

    # 방 생성자가 맞는지 확인
    if lobby.created_by != user.user_id:
        raise HTTPException(status_code=403, detail="오직 방 생성자만 매칭 완료를 실행할 수 있습니다.")

    # 대기실에 있는 모든 유저 정보를 매칭 테이블에 저장
    lobby_users = match_db.query(LobbyUserModel).filter(LobbyUserModel.lobby_id == lobby_id).all()
    mate_ids = ",".join([str(user.user_id) for user in lobby_users])

    # 매칭 정보 업데이트
    matching = match_db.query(MatchingModel).filter(MatchingModel.id == lobby.matching_id).first()
    if matching:
        matching.mate = mate_ids
        match_db.commit()

    match_db.query(LobbyUserModel).filter(LobbyUserModel.lobby_id == lobby_id).delete()

    match_db.delete(lobby)
    match_db.commit()

    return {"message": "대기실이 정상적으로 완료되었습니다."}


@router.post("/matchings/{matching_id}/complete", response_model=dict)
def complete_drive(
    matching_id: int,
    credentials: HTTPAuthorizationCredentials = Security(security),
    user_db: Session = Depends(get_userdb),
    match_db: Session = Depends(get_matchdb),
    history_db: Session = Depends(get_historydb)
):
    user = get_current_user(credentials, user_db)

    # 매칭 정보 가져오기
    matching = match_db.query(MatchingModel).filter(MatchingModel.id == matching_id).first()
    if not matching:
        raise HTTPException(status_code=404, detail="매칭을 찾을 수 없음")

    lobbies = match_db.query(LobbyModel).filter(LobbyModel.matching_id == matching_id).all()
    if lobbies:
        raise HTTPException(status_code=400, detail="매칭에 연관된 대기실이 아직 존재합니다. 먼저 모든 대기실을 완료하세요.")

    # History에 저장할 데이터 생성
    history_data = HistoryCreate(
        car_num="차량번호",
        date=datetime.now(), 
        boarding_time=matching.boarding_time.strftime("%H:%M"),  
        quit_time=datetime.now().strftime("%H:%M"),  
        amount=10000, 
        depart=matching.depart,
        dest=matching.dest,
        mate=matching.mate  
    )

    create_history(history=history_data, credentials=credentials, db=history_db)

    # 매칭 삭제
    match_db.delete(matching)
    match_db.commit()

    return {"message": "운행이 완료되어 매칭 정보가 기록되었습니다."}
