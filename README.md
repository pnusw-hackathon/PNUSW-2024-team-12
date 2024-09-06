
- 목차
> [1. 프로젝트 소개](#1-프로젝트-소개) <br/> 
> [2. 상세설계](#2-상세설계) <br/>
> [3. 개발 결과](#3-개발결과) <br/>
> [4. 설치 및 사용 방법](#4-설치-및-사용-방법) <br/>
> [5. 소개 및 시연 영상](#5-소개-및-시연-영상) <br/>

### 1. 프로젝트 소개
#### 가. 개발배경 및 필요성

**1 ) 부산대학교 순환버스(금정7)는 만성적인 공급 부족 문제에 시달리고 있으며, 안전사고 발생 가능성이 높음.**
  - **순환버스 내 다중밀집 사고 우려**
    - 우리 대학 총학생회 측의 22년도 조사에 따르면, 기점인 부산대역의 등교 시간대의 대기인원은 최대 81명에 육박하며, 등교 시간대 탑승인원이 최대 65명임을 알 수 있음.
    <img src="/img/표1_순환버스 현황조사.png" width="800px" title="Title" alt="Alt text"></img>
    - 특히 우리 대학 순환버스(현대 뉴 슈퍼 에어로시티)의 제조사 규정 최대 탑승인원은 43명인데, 이보다 1.5배나 더 많은 인원이 피크타임인 23분 이후로 계속 탑승하고 있음.
    이처럼 순환버스 내 탑승 인원이 너무 많다 보니, 순환버스 내 다중밀집사고 우려도 지속적으로 제기되고 있으며(채널PNU, 2022. 11. 03 보도), 많은 사람이 밀집해서 탑승하다 보니 전반적인 순환버스 만족도로 굉장히 낮음.
  - **열악한 순환버스 이외에 선택지가 없는 학생들**
    <img src="/img/표2_순환버스만족도.png" width="800px" title="Title" alt="Alt text"></img>
    - 우리 대학 총학생회가 2023년에 학생 701명을 대상으로 시행한 설문조사에 따르면, 전반적인 순환버스 이용 환경에 대한 만족도가 10점 만점에 5.02점으로 매우 낮은 편이고, 우리 팀이 부산캠퍼스 학생 101명을 대상으로 시행한 설문조서에서도 순환버스 이용 중 불편함을 느꼈다고 답한 학생이 90%로 대다수의 학생들이 현재의 순환버스 환경에 많은 불편함을 느끼고 있음.
      그럼에도 불구하고 위와 같이 많은 학생들이 이용하고 있는데, 결국 이는 순환버스 이용 환경  경사가 심한 우리 대학 부산캠퍼스의 특성, 부산대역과 캠퍼스 간 먼 거리 등의 복합적인 사유로 인해 학생들이 반강제적으로 순환버스를 탑승하고 있다고 볼 수 있음.
  - **기대할 수 없는 순환버스 증차**
    - 코로나19 펜데믹의 직격탄을 맞은 대영버스측의 순환버스 증차도 기대할 수 없는 실정임. 원래부터 대영버스에 따르면 무료 환승 탑승객이 다수를 차지하는 순환버스는 요금을 내지 않는 승객이 40%에 달해 노선 자체가 구조적으로 문제가 있는데다, 코로나19 펜데믹 이전에도 지속적으로 만성적인 적자를 호소하고 있었기 때문임(채널PNU, 2014.05.19. 보도).
  - **빈번한 탑승 거부**
    <img src="/img/원형차트1_순환버스탑승거절.png" width="800px" title="Title" alt="Alt text"></img>
    - 결국 이와 같은 상황에서 순환버스를 탑승하지 못하는 사례도 생기고 있음. 우리 팀에서 자체적으로 실시한 설문조사에 따르면 부산캠퍼스 학생 101명 중 41%에 달하는 학생들이 순환버스 탑승 거부를 당한 경험이 있는데, 부산대역에서 이미 만차가 된 상태에서 다음 역으로 버스가 출발하기 때문임. 결국 탑승 거부를 당한 학생들은 수업 시간에 맞추기 위하여 택시를 타게 되며 이로 인한 경제적인 부담이 발생함.

**2 ) 인상된 택시 요금으로 인한 우리 대학 학생들의 경제적 부담 증가**
  - 2023년을 기점으로 부산택시의 기본 요금이 3,800원에서 4,800원으로 인상되었고, 거리요금과 시간요금도 덩달아 소폭 인상되었음. 더불어 심야할증 시간 역시 1시간 앞당겨졌으며 자정부터 오전 2시까지는 기존의 20% 할증이 아닌 30% 할증을 적용하게 되었음.(부산일보, 2023. 05. 12. 보도)
    그런데 우리 대학 학생들의 택시 수요는 굉장히 많은 편임. 현직 택시 기사 경력 11년차인 A씨는 “오후 11시가 넘어가면 부산대학교 앞에서 집으로 가는 택시를 타는 학생들이 굉장히 많다.”면서, 심야 시간 대에 우리 대학 근처에서 콜 대기를 하는 경우도 적지 않다고 답하였음.
  - 실제로 오후 10시 이후 우리 대학 앞 부산대학교 사거리에 가보면, 늦은 시간에 막차가 끊겨 택시를 타러 나오는 학생들을 기다리는 택시가 4, 5대씩 계속 대기하고 있으며, 이외에도 주요 상권인 부대앞삼거리 및 그 아래 골목에도 택시가 1, 2대씩 대기하고 있는 광경을 볼 수 있음.
  <img src="/img/그래프1_택시이용률.png" width="800px" title="Title" alt="Alt text"></img>
  - 더불어 자체적으로 실시한 설문조사 결과에 따르면, 부산캠퍼스 학생 101명 중 37명은 택시를 주로, 많이 이용한다고 답하였으나, 택시 요금 적절도에 관한 질문에는 78명이 ‘매우 적절하지 않음‘, 혹은 ’적절하지 않음‘을 선택하였음.
  - 이처럼 많은 택시 수요에 비해 인상된 택시 요금은 학생들의 경제적 부담을 가중시키고 있음. 이에 비슷한 목적지를 가진 학생들끼리 택시를 함께 탐으로 학생들의 경제적 부담을 덜어주고, 신원이 확인된 우리 대학 학생들끼리 택시를 공유하여 안전한 귀가를 할 수 있도록 하고자 함.

**3 ) 밀양캠퍼스-밀양역 간 이동 수단 문제**
  - 현재 밀양역-밀양캠퍼스 간 현존하는 대중교통은 버스뿐으로, 배차간격이 평일 1~2시간 간격이라 밀양캠퍼스 학생들의 이동 수단이 굉장히 부족한 상황임.
    
    <img src="/img/밀양-밀양캠 버스 충족도.png" width="800px" title="Title" alt="Alt text"></img>
    
  - 자체 설문조사 결과에 따르면, 밀양캠퍼스 재학생 97명 중 87명(89.7%)에 달하는 학생들이 멸양역-밀양캠퍼스 간 버스의 공이 전혀 충분하지 않거나 다소 충분하지 않다고 답하였음.
  - 더불어 밀양역-밀양캠퍼스 간 택시 요금 또한 큰 문제임. 밀양캠퍼스의 경우 밀양시 삼랑진읍에 위치하여 있는데, 삼랑진읍을 오는 과정에서 시외할증 요금이 적용돼 차로 5분이라는 짧은 거리임에도 불구하고 택시비가 7~8,000원씩이나 하는 상황임. 심지어 야간에는 야간할증까지 붙어 10,000원대까지 올라가기도 함.
    
    <img src="/img/밀양-밀양캠 택시요금 적절도.png" width="800px" title="Title" alt="Alt text"></img>
    
      - 이러한 할증 요금에 대한 문제 때문에, 밀양캠퍼스 학생들의 택시 요금에 대한 불만은 부산캠퍼스 학생에 비해 훨씬 심함. 자체 설문조사 결과에 따르면 밀양캠퍼스 학생 97명 중 92명(94.8%)이 밀양캠퍼스-밀양역 간 택시 요금이 매우 부적절하거나 다소 부적절하다고 답하였음.

*** 

#### 나. 개발 목표 및 주요 내용

**1 ) 개발목표**

&emsp;**1-1) 순환버스 공급 부족 문제 해결을 학생들에게 안전하고 편안한 이동 수단 제공**
   - 앞서 말했듯 우리 대학 순환버스 공급 부족으로 인한 안전 문제 및 만족도 문제를 공유 택시 서비스라는 선택지를 학생들에게 제공함으로서 해결할 수 있음.

&emsp;**1-2) 학생들의 경제적 부담 절감**
   - 부산대역에서 출발한다고 가정할 시, 우리 대학 대부분의 건물은 기본요금인 4,800원 이내로 갈 수 있음. 이를 최대 4인이서 나누어 결제할 수 있도록 하여, 대중교통과 거의 같은 금액에 택시를 이용할 수 있도록 함.
   - 또한 버스 배차간격이 길어 택시 수요가 많은 밀양캠퍼스-밀양역 간 구간서 학생들끼리 과도한 택시 요금을 나누어 결제함으로서 밀양캠퍼스 학생들의 경제적 부담을 상당 부분 절감할 수 있음.

&emsp;**1-3) 지역 택시 운수사와의 협력을 통한 경제 활성화 및 운용 택시 확보**
   - 카카오택시 등의 대형 플랫폼 기업에 많은 어려움을 겪고 있는 지역 운수사과 협력함.
   - 이를 통하여 BRR은 택시 기사를 확보하고, 운수사는 해당 수요를 가져갈 수 있도록 하는 상호 협력적 관계를 구축함.

&emsp;**1-4) 부산대학교 학생들만을 위한 공공 서비스 개발**
   - 믿고 신뢰할 수 있는 신원이 검증된 우리 대학 학생들끼리만 택시를 공유하여, 안전한 탑승 환경을 조성함.
   - 뿐만 아니라 시간표 등록과 같은 부산대학교 학생이라는 특수성을 반영한, 학생들에게 최적화된 서비스를 제공함.

**2 ) 주요내용**

&emsp;**2-1) 택시 매칭 서비스**
   - 유저들이 택시를 타고 가고자 하는 출발지와 목적지를 앱에 등록하면, 출발지와 목적지가 비슷한 유저들을을 매칭시켜 함께 탈 수 있도록 함.
   - 매칭 시에는 크게 '빠른 매칭'과 '매칭 예약' 두 가지 종류로 나뉘어 매칭이 됨,
     - 빠른 매칭: 매칭 시작 시 즉시 매칭을 하며, 매칭이 완료되면 바로 택시를 탈 수 있음
     - 매칭 예약: 택시를 타야 하는 시간대에 예약을 하여 미리 매칭을 한 후에 해당 시간대에 바로 탑승할 수 있도록 함.
   - 매칭이 완료되고 택시를 호출하면 해당 시점 콜 대기중인 기사 앱에 표시됨.
     - 이때 기사는 출발지, 목적지, 현재 위치로부터 거리, 예상 요금 등을 알 수 있음.

&emsp;**2-2) 자동결제 서비스**
   - 등록된 결제수단(카드, 페이 등)을 통해 함께 택시를 탄 사람과 N분의 1이 된 가격을 자동 결제함.
   - 결제된 금액은 한데 모아, 결제 이후 기사에게 3 영업일 이후 자동이체 됨.

&emsp;**2-3) 채팅 서비스**
   - 매칭된 유저들끼리 현재 위치 등의 정보를 공유할 수 있도록 채팅 서비스를 제공함
   - 채팅방는 매칭이 시작될 때 개설되며 매칭이 종료된 이후에 자동으로 삭제됨.

&emsp;**2-4) 시간표 등록 및 목적지 추천 서비스**
   - 본인 시간표 일정에 맞추어, 목적지를 자동으로 설정하여 추천해주는 서비스를 제공함.
   - 시간표에는 수업 일정 말고 개인 일정도 추가할 수 있으며, 이를 통해 개인 일정에도 맞추어 목적지를 추천해 줌.

&emsp;**2-5) 학생 인증 서비스**
   - 부산대학교 웹메일을 활용하여 회원가입 시 부산대학교 학생인지 인증하도록 함.
     - 이는 추후에 실제로 런칭하게 된다면 정보화본부와 협력하여 학생지원시스템 아이디 및 비밀번호를 활용한 인증 절차도 도입할 예정임.

&emsp;**2-6 ) 기타 서비스 이용을 원활하게 하기 위한 서비스**
   - 마이페이지에서 이용 기록을 확인할 수 있으며, 이용 기록에서는 탑승한 택시 번호, 택시를 같이 탄 사람 등의 정보를 확인할 수 있음.
   - 택시가 배정되면 기사에게 바로 연락할 수 있도록 연락처를 제공함
   - 기사의 경우 추후에 실제로 런칭하게 된다면 운수사업자등록여부 등의 추가 인증 절차를 도입할 예정임.
   
***

#### 다. 세부내용

> 더 자세한 기능 설명은 개발결과의 기능설명 참고

> 사용자(손님) 기능

  **1 ) 택시 호출**
   - 사용자들을 매칭한 후 택시를 호출할 수 있음.

  **2 ) 매칭 서비스**
   - 출발지가 비슷한 위치의 유저들이, 목적지가 비슷한 경우 택시를 함께 탈 수 있도록 매칭해주는 서비스
   - 매칭 시 최소인원을 선택할 수 있음.
   - 매칭 방식은 빠른 매칭 / 예약 매칭으로 나뉨
   - 빠른 매칭: 매칭 시작 시 즉시 매칭을 하며, 매칭이 완료되면 바로 택시를 탈 수 있음
   - 매칭 예약: 택시를 타야 하는 시간대에 예약을 하여 미리 매칭을 한 후에 해당 시간대에 바로 탑승할 수 있도록 함.
   - 매칭이 진행 중일 때는 *매칭 대기 페이지*에서 대기하며, *출발해요*버튼을 클릭할 경우 택시를 호출
   - 타 사용자는 *매칭 목록 페이지*을 통해 현재 모집 중인 빠른 매칭과 예약매칭 목록을 확인할 수 있고, 클릭할 경우 *매칭대기 페이지*로 이동할 할 수 있음.
    
**3 ) 매칭 커뮤니티**
   - 출발지로 모이기 위해 매칭된 유저들끼리 소통할 수 있도록 채팅방를 개설.
   - 해당 커뮤니티는 택시 하차 후 자동 삭제.

 **4 ) 매칭 목록**
   - 사용자는 택시호출을 직접하지 않아도 *매칭 목록 페이지*를 들어가 매칭 목록을 확인할 수 있음.
   - 목록을 클릭하면 매칭이 되고, *매칭대기페이지*로 이동
   - *매칭 목록 페이지*에는 빠른매칭과 예약매칭을 선택할 수 있음.
   - 도착지를 검색했을 경우, 검색 조건에 맞는 목록을 보여줌. 
   - 매칭 목록에는 출발지, 목적지, 탑승시간등의 정보들이 있음.

**5 ) 자동결제 서비스**
   - 등록된 결제수단(카드, 페이 등)을 통해 함께 택시를 탄 사람과 N분의 1이 된 가격을 자동 결제함.
   - 결제된 금액은 한데 모아, 결제 이후 기사에게 3 영업일 이후 자동이체 됨.

**6 ) 시간표 등록**
   - 부르릉은 부산대생에 한정하여 배포할 예정이다. 이에 따라 시간표를 등록하면 *메인페이지*의 *목적지 추천*에서 어느 건물로 가야하는지 자동으로 볼 수 있다
   - *목적지 추천*을 클릭하면 *매칭 페이지*로 이동하여 자동으로 목적지가 정해진다.
    
**7 ) 본인확인**
  - 회원가입은 학번과 비밀번호를 통해 진행한다. 
  - 학생증 사진을 첨부하여 소속인증을 진행한다. 
  - 전화번호 인증을 한다. 

**8 ) 마이페이지**
  - 회원 정보  : 아이디와 비밀번호를 관리
  - 시간표 관리 : 시간표를 등록하고 관리
  - 이용기록 : 탑승시간, 하차시간, 금액, 출발지, 목적지 등 부르릉 사용에 관련된 이용기록

**9 ) 로그인 및 회원가입**
  - 부르릉을 사용하기 위해서는 회원가입이 필요
  - 회원가입을 할 때 사용자인지 택시기사인지 선택
  - 회원가입 정보는 이름, 아이디, 비밀번호, 전화번호 등으로 구성
 

> 택시기사 기능

**1 ) 호출 받기**
  - 회원가입을 할 때 택시기사라고 선택했을 경우 이 기능이 추가
  - 택시기사는 *택시기사 페이지*와 *콜대기 및 콜수락 페이지* 등을 통해 호출을 받음
  - 택시기사 전용 마이페이지를 통해 기사정보를 관리할 수 있음.

***

#### 라. 기존 서비스 대비 차별성

> 기존의 택시 호출 서비스는 카카오택시, 우버택시, 동백콜 등이 있음. 이들과의 차이점은 다음과 같음

  **1 ) 함께 탈 수 있도록 하는 공유 택시 서비스**
   - 타 서비스 대비 BRR의 가장 큰 차별성임. 함께 택시를 탑승함으로서 택시 요금을 절감할 수 있고, 이는 다른 택시 어플에서는 찾아볼 수 없는 기능임.
   - 이를 통해 학생들에게 쾌적하고 안전한 이동수단을 저렴한 가격에 이용할 수 있도록 함.
   - 이러한 기능은 특히 대중교통이 없고 여러 할증으로 인해 택시 요금이 비싼 밀양캠퍼스와 같은 교통소외지역에서 많은 수요를 얻을 수 있음.
     
  **2 ) 선별된 이용자**
   - 1.에서 언급하였던 함께 택시를 탑승하는 서비스가 타 택시 어플에서 찾아보기 힘든 이유는 아무래도 안전 문제 때문임. 신원이 정확히 파악되지 않은 낯선 이와 택시를 함께 탑승한다는 것은 위험 요소가 너무 많음.
   - 그러나 BRR은 서비스 대상을 '부산대학교 학생'으로 한정하였고, 이에 대한 인증 절차를 추가함으로서 탑승자에 대한 정확한 신원을 파악할 수 있도록 하였고 '부산대학교'라는 공동체에 소속된 자에게만 서비스를 제공함으로서 보다 안전하고 믿을 수 있는 택시 탑승 환경을 조성하였음.
     
  **3 ) 지역사회와 협력하는 공공 서비스**
   - BRR은 부산대학교 학생을 위한 공공 서비스로, 수익보단 공익을 택한 서비스임
   - 즉, 수수료 징수 등의 추가 요금 없이 무료로 택시 기사들에게 서비스를 제공한다는 뜻이며, 이는 택시기사 입장에서 충분히 매력적인 요소로 작용할 수 있음.
   - 더불어 카카오택시 등의 대형 플랫폼 기반 택시 어플의 등장으로 사정이 어려운 지역 사회의 운수사에 무료로 서비스를 제공하여 택시 기사를 확보할 수 있으며, 운수사의 입장에서는 수입에 도움을 받을 수 있음.
   
***

#### 마. 사회적가치 도입 계획

  **1 ) 안전한 교통 환경 조성 및 학생 복지 증진**
   - 순환버스 탑승자 수를 줄임으로서 밀집도를 완화, 학생들의 안전한 순환버스 이용환경을 만드는 데 이바지함.
   - 더불어 개개인의 택시 요금을 절감함으로서 학생들의 경제적 부담을 완화하고, 순환버스 배차간격이 긴 야간 시간에도 편안하고 안전한 이동 수단을 제공함.
     
  **2 ) 환경 보호에 기여**
   - 택시를 공유함으로서 탄소 배출량을 줄여 환경 보호에 기여할 수 있음
     
  **3 ) 지역 사회 경제 활성화**
   - 지역 운수사와 협력하여 서비스를 제공함으로서 지역 경제에 이바지함.

### 2. 상세설계
#### 가. 시스템 구성도

<p align="center"> 
<img src="/img/시스템 구성도.png" width="800px" title="Title" alt="Alt text"></img>
</p>

#### 나. 사용 기술
> 스택 별(backend, frontend, designer등) 사용한 기술 및 버전을 작성하세요.

|이름|버전|
|:---:|:----------------------------:|
| python  | 3.12      | 
| mariadb  | 11.2         | 
| fastapi  | 0.111.0        | 
| SQLAlchemy  |  2.0.30           |
| websocket-client  |  1.8.0    |

### 3. 개발결과
#### 가. 전체시스템 흐름도
&emsp;**1 ) IA(Information Architecture)**
   > BRR의 구조를 도식화
   
   BRR은 사용자(손님)와 택시기사로 구분하여 페이지가 구성됨
   <p align="center"> 
   <img src="/img/IA.jpg" width="800px" title="Title" alt="Alt text"></img>
   </p>
   
&emsp;**2 ) 유저 플로우 차트**
   
   &emsp;&emsp;**2-1) 사용자 전체 플로우 차트**
   > 사용자의 전체 플로우 차트

   사용자(손님)는 사람들을 매칭하는 방을 만들어 택시를 호출할 수 있고, *매칭 목록 페이지*에서 이미 만들어진 방에 참여할 수 있음
   
   또한 시간표 등록을 통해 *메인페이지*에서 시간표에 따른 추천 도착지도 설정할 수 있음
   <p align="center"> 
   <img src="/img/brr 사용자 전체 페이지.jpg" width="800px" title="사용자 전체 플로우 차트" alt="Alt text"></img>
   </p>

   &emsp;&emsp;**2-2) 기사 전체 플로우 차트**
   > 택시기사의 전체 플로우 차트

   기사는 *출근하기* 버튼을 클릭하면 *콜 대기 페이지*으로 이동하여 사용자가 택시를 부르면 자동으로 리스트업이 되어 콜 수락을 할 수 있음.
   <p align="center"> 
   <img src="/img/brr 기사 전체 페이지.jpg" width="400px" title="기사 전체 플로우 차트" alt="Alt text"></img>
   </p>
   
   &emsp;&emsp;**2-3) 회원가입 플로우 차트**
   > 회원가입 플로우 차트
   >
   > 왼쪽은 사용자의 회원가입 과정, 오른쪽은 택시기사의 회원가입 과정

   사용자는 부산대 학생으로 제한하기 때문에 학번과 이메일 인증 과정을 거침
   
   <p align="center"> 
   <img src="/img/전체 회원가입 플로우 차트.jpg" width="800px" title="회원가입 플로우 차트" alt="Alt text"></img>
   </p>

&emsp;**3 ) 테스크 플로우 차트**
 
   &emsp;&emsp;**3-1) 로그인 및 회원가입 플로우 차트**
   > 로그인과 회원가입의 플로우 차트

   회원가입 시 사용자(손님)과 택시기사로 나뉨
   
   사용자는 아이디, 비밀번호, 이름, 전화번호, 학번, 이메일의 정보를 입력함.
   
   택시기사는 아이디, 비밀번호, 이름, 전화번호, 자동차 번호, 자동차 모델을 입력함.
   
   로그인 시 사용자일 경우 *사용자 페이지*로, 택시 기사의 경우 *택시 기사 페이지*로 이동함.
   <p align="center"> 
   <img src="/img/brr 로그인 및 회원가입 플로우 차트.jpg" width="800px" title="brr 로그인 및 회원가입 플로우 차트" alt="Alt text"></img>
    </p>
    
&emsp;**4 ) 시스템 플로우 차트**
 
   &emsp;&emsp;**4-1) 이메일 인증 플로우 차트**
   > 이메일 인증 플로우 차트

   사용자가 회원가입을 진행할 때 이메일을 입력한 후 *전송* 버튼을 클릭하면 인증번호가 SMTP서버를 통해 전송됨

   받은 이메일을 입력한 후 일치하면 이메일 인증이 성공됨
   
   <p align="center"> 
   <img src="/img/brr 이메일 인증 플로우 차트.jpg" width="800px" title="Title" alt="Alt text"></img>
   </p>
   
   &emsp;&emsp;**4-2) 매칭 플로우 차트**
   > 매칭 플로우 차트

   사용자 1이 매칭을 만들 때 출발지, 도착지, 인원 등을 선택하여 방을 개설(매칭)

   방이 만들어지면 타 사용자는 *매칭 목록 페이지*에서 해당 방에 참여할 수 있음
   
   이후 현재 인원이 최소 인원을 만족하면 방장이 *출발해요* 버튼을 클릭할 수 있고 택시를 호출함. 

   택시기사는 호출된 리스트를 *콜 대기 페이지*에서 볼 수 있고 콜을 수락하면 택시를 탈 수 있음.

   탑승 후 하차한 경우 택시기사가 *운행 종료* 버튼을 클릭하면 매칭 과정이 종료되고 이용기록이 저장됨.
   
   <p align="center"> 
   <img src="/img/brr 매칭 플로우차트.jpg" width="800px" title="Title" alt="Alt text"></img>
   </p>
   
   &emsp;&emsp;**4-3) 결제 로직**
   > 결제 플로우 차트입니다.

   방장이 *출발해요* 버튼을 클릭하면 각 사용자들이 미리 결제를 하여 소유금액을 확인.
   
   예상금액/n + 10%의 가격의 조건을 만족하지 않으면 결제가 실패되고 택시 호출이 실패 

   만약 조건이 만족되면 각 사용자들에게 환불함

   이후 운행이 완료되면 실제금액을 바탕으로 n등분한 가격을 결제함 
   <p align="center"> 
   <img src="/img/결제 플로우 차트.jpg" width="800px" title="결제 플로우 차트" alt="Alt text"></img>
   </p>
   
&emsp;**5 ) ERD**

   &emsp;&emsp;**5-1) database ERD**
   > BRR 전체 database ERD입니다. 
   >> user_info : 사용자와 택시기사의 유저 정보들이 있는 테이블
   >> 
   >> lobbies : 매칭이 완료되기 전 임시로 만들어 지는 테이블
   >> 
   >> lobby_user : 어떤 방에 어떤 유저가 있는 지 확인하는 테이블
   >>
   >> matching : 매칭이 된 방들의 테이블
   >>
   >>history : 운행이 종료된 후 이용기록이 저장되는 테이블
   >>
   >> taxes : 택시의 정보가 있는 테이블
   >>
   >> email_codes : 이메일 인증 코드를 임시로 저장하는 테이블 
   
   <p align="center"> 
   <img src="/img/ERD.jpg" width="800px" title="Title" alt="Alt text"></img>
   </p>



#### 나. 기능설명

**1 ) 회원가입**
   > 회원가입은 사용자와 기사로 나뉨

&emsp;**1-1) 사용자 회원가입**
   - 아이디와 비밀번호, 비밀번호 확인, 전화번호, 학번, 이메일 입력
   - *전송*버튼을 클릭하면 이메일로 인증번호 발송
   - 인증번호 작성 후 *확인*버튼 클릭
   - 인증번호가 일치하지 않을 시 재전송 가능
   - 인증번호가 일치할 경우 *회원가입*버튼 클릭
   - 아이디, 전화번호, 학번, 이메일 등의 중복 검사 실시
   - 비밀번호 확인과 비밀번호가 일치 검사 실시
   - 오류가 있을 경우 재입력
   - 검사를 통과하면 회원가입 성공

&emsp;**1-2) 기사 회원가입**
  - 아이디, 비밀번호, 비밀번호 확인, 전화번호, 자동차 번호, 자동차 모델 입력
  - 아이디, 전화번호, 자동차 번호, 자동차 모델 등의 중복 검사 실시 
  - 비밀번호 확인과 비밀번호가 일치 검사 실시
  - 오류가 있을 경우 재입력
  - 검사를 통과하면 회원가입 성공

&emsp;**1-3 ) 이메일 인증**
  - 전송버튼을 클릭하면 아이디와 이메일의 중복 검사 실시
  - 중복이 아닐 경우 작성한 이메일로 SMTP를 이용하여 인증번호 전송
  - 인증번호를 입력한 후 *확인*버튼 클릭
  - 인증번호가 일치할 시 인증 완료
  - 불일치할 시 재인증




&emsp;**2 ) 로그인**
- 회원가입을 한 후 아이디와 비밀번호를 입력한 후 계정이 있는지 확인
- 계정이 없으면, 경고문구가 나타남
- 계정이 있는 경우 user type이 사용자인 경우 *사용자 페이지*로, 택시기사인 경우 *택시 기사 페이지*로 이동함

https://github.com/user-attachments/assets/4bb5e971-b62a-4b6f-9045-67f0c4ceb874
  
&emsp;**3 ) 예약 목록**
- 사용자가 참여하고 있는 매칭 목록을 볼 수 있음
  
&emsp;**4 ) 시간표 등록 -> 목적지 추천**

- *마이페이지* -> *시간표 등록*에서 시간표를 등록
- 날짜, 시간, 장소, 수업 명의 정보를 작성하면 시간표에 추가됨
- 등록한 시간표에 따라 *메인페이지*의 *목적지 추천*에 시간표에 해당하는 목적지를 자동으로 추천
- *목적지를 이곳으로 선택* 버튼을 클릭하면 매칭화면으로 넘어가 도착지를 자동으로 설정


https://github.com/user-attachments/assets/6ac487c6-1036-456b-be69-1e8cdd0bbcad

  
&emsp;**5 ) 매칭 목록**
- 예약 목록은 빠른 매칭과 매칭 예약으로 나뉨
- 빠른 매칭에 들어가면 빠른 매칭의 목록들을 볼 수 있음
- 매칭 예약에 들어가면 매칭 예약의 목록들을 볼 수 있음
- 탑승하고 싶은 목록을 클릭하면 매칭에 합류





&emsp;**6 ) 빠른 매칭**
- *메인페이지*의 *빠른 매칭* 버튼을 클릭하면 *빠른 매칭 페이지*로 이동
- 출발지와 도착지를 입력하면 소요시간, 예상 금액, 이동 경로, 지도 등이 표시
- 최소인원을 설정하고 *매칭 시작하기*버튼을 클릭하면 매칭이 시작
  
&emsp;**7 ) 매칭 예약**
- *메인페이지*의 *매칭 예약* 버튼을 클릭하면 *매칭 예약 페이지*로 이동
- 탑승할 날짜와 시간을 지정
- *다음 단계로 넘어가기* 버튼을 클릭
- 출발지와 도착지를 입력하면 소요시간, 예상 금액, 이동 경로, 지도 등이 표시
- 최소인원을 설정하고 *매칭 시작하기*버튼을 클릭하면 매칭이 시작

https://github.com/user-attachments/assets/14b638f0-ce33-4c31-bb9f-9cfa0b518a8b

&emsp;**8 ) 채팅**
- 매칭 대기화면에서 채팅버튼을 클릭하면 채팅화면으로 이동
- 채팅을 통해 현재 위치를 공유할 수 있음
- 택시 하차 후 채팅방 자동 제거  

&emsp;**9 ) 이용기록**
- 운행이 종료되면 자동으로 이용기록이 저장
- *마이페이지*의 *이용기록 확인*에서 확인
- 자동차 번호, 탑승 날짜, 시간, 출발지, 도착지, 금액 등의 정보 확인
- 디테일한 정보를 확인하고 싶을 경우 해당 이용내역을 클릭
- 자동차 모델, 기사 이름, 같이 탄 사람 등을 추가로 확인 가능

&emsp;**10 ) 출근하기**
- 택시기사의 기능으로 *출근하기* 버튼을 클릭할 시 *콜 대기 페이지*로 이동

&emsp;**11 ) 콜 대기 및 콜 수락**
- 사용자(손님)이 택시를 호출하면 *콜 대기 페이지*에 해당 정보가 올라감
- 기사는 해당 콜을 클릭하면 *콜 수락 페이지*로 이동
- *수락하기*를 클릭하면 매칭이 완료
- 손님이 목적지에 하차한 후 운행 완료하면 이용 내역이 저장됨
  
#### 다. 기능명세서
> BRR의 주요 기능

&emsp;**1 ) 회원가입**
<p align="center"> 
<img src="/img/다_회원가입.png" width="500px" title="Title" alt="Alt text"></img>
</p>

<div align="center"> 
   
|라벨|이름|상세|
|:---:|:----------------------------:|:---|
| S0  | 회원 종류 선택            | - 사용자/택시기사 회원가입 선택 |
| S1  | 이름            | - 이름 입력 |
| S2  | 아이디              | - 아이디 입력 <br/> - 중복되는 아이디인지 검증 |
| S3  | 비밀번호 | - 비밀번호 입력 |
| S4  | 비밀번호 확인                 | - 비밀번호 일치 검증 |
| S5  | 전화번호 입력            | - 전화번호 입력 <br/> - 중복되는 전화번호인지 검증 |
| S6  | 학번 입력                        | - 학번 입력 <br/> - 중복되는 학번인지 검증 |
| S7  | 부산대학교 웹메일                 | - 부산대 웹메일 형식인지 검증 <br/> - 중복되는 이메일인지 검증 |
| S8  | 부산대학교 웹메일 인증번호 전송                   | - 클릭 시 인증 번호 메일로 전송 |
| S9  | 메일 인증번호                      | - 인증번호 입력 |
| S10 | 메일 인증번호 확인                 | - 인증번호 일치 검증 |
| S11 | 기사 차 번호                | - 기사 차 번호 입력 <br/> - 중복되는 차 번호인지 검증 |
| S12 | 기사 사 모델                 | - 기사 차 모델 입력 |
| S13 | 가입하기                  | - 비어 있는 입력 칸이 없는지 검증 <br/> - 메일 인증 완료했는지 확인 <br/> - 조건을 만족하면 회원가입 성공|
| S14 | 로그인                        | - 클릭 시 *로그인 페이지*로 이동 |

</div>

***

&emsp;**2 ) 로그인**
<p align="center"> 
<img src="/img/다_로그인 페이지.png" width="200px" title="Title" alt="Alt text"></img>
</p>

<div align="center"> 

|라벨|이름|상세|
|:---:|:----------------------------:|:---|
| S0 | 아이디            | - 아이디 입력 <br/> - 유효성 검사  |
| S1 | 비밀번호              | - 비밀번호 입력 <br/> - 유효성 검사 |
| S2 | 로그인 완료 | - 비어 있는 입력 칸이 없는지 검증 <br/> - 조건을 만족하면 로그인 성공  |
| S3 | 아이디/비밀번호 찾기               | - 클릭 시 *아이디/비밀번호 찾기 페이지*로 이동 |
| S4 | 회원가입                        | - 클릭 시 *회원가입 페이지*로 이동 |

</div>

***

&emsp;**3 ) 메인페이지**
<p align="center"> 
<img src="/img/다_메인 페이지.png" width="200px" title="Title" alt="Alt text"></img>
</p>

<div align="center"> 

|라벨|이름|상세|
|:---:|:----------------------------:|:---|
| S0 | 빠른 매칭            | - 클릭 시 *빠른 매칭 페이지*로 이동  |
| S1 | 매칭 예약              | - 클릭 시 *매칭 예약 페이지*로 이동 |
| S2 | 예약 목록          | - 예약한 매칭 목록 확인 <br/> - 클릭 시 *매칭 대기 페이지*로 이동 |
| S3 | 목적지 추천               | - 시간표에 따른 도착지 추천 <br/> - 클릭 시 *시간표*로 이동 |
| S4 | 매칭 목록                        | - 참여할 수 있는 매칭 목록 <br/> - 클릭 시 *매칭 목록 페이지*로 이동|
| S5 | 매칭 목록(네비게이션)                        | - 클릭 시 *매칭 목록 페이지*로 이동 |
| S6 | 홈                       | - 클릭 시 *홈 페이지*으로 이동 |
| S7 | 마이페이지                     | - 클릭 시 *마이페이지* 로 이동 |

</div>

***

&emsp;**4 ) 빠른 매칭**
<p align="center"> 
<img src="/img/다_빠른매칭.png" width="500px" title="Title" alt="Alt text"></img>
</p>

<div align="center"> 

|라벨|이름|상세|
|:---:|:----------------------------:|:---|
| S0 | 출발지            | - 출발지 검색 기능  |
| S1 | 도착지              | - 도착지 검색 기능 |
| S2 | 최소 인원 선택          | - 최소 인원 선택 기능 |
| S3 | 매칭 시작               | - 택시에 함께 탈 사용자를 매칭 <br/> - 클릭 시 *매칭 대기 페이지*로 이동 |

</div>

***

&emsp;**5 ) 매칭 예약**
<p align="center"> 
<img src="/img/다_매칭예약.png" width="500px" title="Title" alt="Alt text"></img>
</p>

<div align="center"> 

|라벨|이름|상세|
|:---:|:----------------------------:|:---|
| S0 | 출발지            | - 출발지 검색 기능  |
| S1 | 도착지              | - 도착지 검색 기능 |
| S2 | 최소 인원 선택          | - 최소 인원 선택 기능 |
| S3 | 매칭 시작               | - 택시에 함께 탈 사용자를 매칭 <br/> - 클릭 시 *매칭 대기 페이지*로 이동 |
| S4 | 날짜 및 시간            | - 택시를 호출할 날짜 및 시간 선택  |
| S5 | 다음 단계          | - 출발지와 도착지를 선택하고 매칭하는 화면으로 이동 |

</div>


***

&emsp;**6 ) 매칭 목록**
<p align="center"> 
<img src="/img/다_매칭 목록.png" width="200px" title="Title" alt="Alt text"></img>
</p>

<div align="center"> 

|라벨|이름|상세|
|:---:|:----------------------------:|:---|
| S0 | 매칭 타입              | - 빠른 매칭 또는 예약 매칭 선택 |
| S1 | 도착지               | - 도착지 입력 |
| S2 | 검색              | - 출발지, 또는 도착지에 따른 매칭 방 탐색 |
| S3 | 매칭 정보          | - 현재 매칭 중인 방의 정보 <br/> - 클릭 시 매칭 참여|

</div>

***

&emsp;**7 ) 마이페이지**
<p align="center"> 
<img src="/img/다_마이페이지.png" width="200px" title="Title" alt="Alt text"></img>
</p>

<div align="center"> 

|라벨|이름|상세|
|:---:|:----------------------------:|:---|
| S0 | 회원 이름              | - 회원의 이름을 나타냄 |
| S1 | 시간표 등록              | - 클릭 시 *시간표 등록 페이지*로 이동 |
| S2 | 회원 정보          | - 클릭 시 *회원 정보 페이지*로 이동 |
| S3 | 이용기록 확인              | - 클릭 시 *이용기록 확인 페이지*로 이동 |
| S4 | 로그아웃          | - 로그아웃 기능 |

</div>

***

&emsp;**8 ) 회원 정보**
<p align="center"> 
<img src="/img/다_회원정보.png" width="200px" title="Title" alt="Alt text"></img>
</p>

<div align="center"> 

|라벨|이름|상세|
|:---:|:----------------------------:|:---|
| S0 | 회원 이름              | - 회원의 이름을 나타냄 |
| S1 | 유저 타입           | - 유저가 사용자(손님)인지 택시 기사인지 확인 |
| S2 | 아이디              | - 유저의 아이디 |
| S3 | 비밀번호 수정란      | - 현재 비밀번호, 새 비밀번호, 확인 입력 |
| S4 | 비밀번호 수정 버튼        | - 비밀번호 수정란 입력 후 버튼을 누르면 수정됨 |

</div>

***

&emsp;**9 ) 시간표**
<p align="center"> 
<img src="/img/다_시간표등록.png" width="200px" title="Title" alt="Alt text"></img>
</p>

<div align="center"> 

|라벨|이름|상세|
|:---:|:----------------------------:|:---|
| S0 | 시간표             | - 시간표 등록시 나타남 |
| S1 | 요일 및 시간             | - 수업의 요일과 시간을 선택 |
| S2 | 수업 장소              | - 수업 장소 입력 |
| S3 | 수업명         | - 수업명 입력 |
| S4 | 추가하기             | - 클릭 시 시간표에 등록 |

</div>

***

&emsp;**10 ) 이용 기록**
<p align="center"> 
<img src="/img/다_이용내역.png" width="500px" title="Title" alt="Alt text"></img>
</p>

<div align="center"> 

|라벨|이름|상세|
|:---:|:----------------------------:|:---|
| S0 | 운행 정보             | - 탑승한 자동차 번호, 날짜, 시간, 출발지, 도착지, 금액의 정보 <br/> 클릭 시 *차량 상세 정보*페이지로 이동 |
| S1 | 디테일         | - 운행 정보의 자세한 내용|
| S2 | 택시 정보            | - 탑승한 택시의 정보 |
| S3 | 같이 탄 사람         | - 같이 탄 사람의 정보 |

</div>


***

#### 라. 디렉토리 구조
> 위 레포지토리의 디렉토리 구조를 설명하세요.

```
├─.idea
├─backend
│  ├─history
│  │  └─__pycache__
│  ├─matching
│  │  └─__pycache__
│  ├─taxi
│  │  └─__pycache__
│  ├─user
│  │  └─__pycache__
│  └─__pycache__
├─brr
│  ├─android
│  │  ├─app
│  │  │  └─src
│  │  │      ├─debug
│  │  │      ├─main
│  │  │      │  ├─kotlin
│  │  │      │  │  └─com
│  │  │      │  │      └─example
│  │  │      │  │          └─brr
│  │  │      │  └─res
│  │  │      │      ├─drawable
│  │  │      │      ├─drawable-v21
│  │  │      │      ├─mipmap-hdpi
│  │  │      │      ├─mipmap-mdpi
│  │  │      │      ├─mipmap-xhdpi
│  │  │      │      ├─mipmap-xxhdpi
│  │  │      │      ├─mipmap-xxxhdpi
│  │  │      │      ├─values
│  │  │      │      └─values-night
│  │  │      └─profile
│  │  └─gradle
│  │      └─wrapper
│  ├─assets
│  │  ├─fonts
│  │  └─images
│  ├─ios
│  │  ├─Flutter
│  │  ├─Runner
│  │  │  ├─Assets.xcassets
│  │  │  │  ├─AppIcon.appiconset
│  │  │  │  └─LaunchImage.imageset
│  │  │  └─Base.lproj
│  │  ├─Runner.xcodeproj
│  │  │  ├─project.xcworkspace
│  │  │  │  └─xcshareddata
│  │  │  └─xcshareddata
│  │  │      └─xcschemes
│  │  ├─Runner.xcworkspace
│  │  │  └─xcshareddata
│  │  └─RunnerTests
│  ├─lib
│  │  ├─constants
│  │  │  └─bottom_navigation
│  │  ├─controller
│  │  ├─design_materials
│  │  ├─layout
│  │  ├─model
│  │  ├─router
│  │  └─view
│  │      ├─chating_page
│  │      ├─driver_page
│  │      ├─history_page
│  │      ├─loading_circle
│  │      ├─loading_page
│  │      ├─location_write_page
│  │      ├─login_page
│  │      ├─main_page
│  │      ├─matching_page
│  │      ├─match_list_page
│  │      ├─mypage_page
│  │      ├─ride_complete_view.dart
│  │      ├─schedule_page
│  │      └─sign_up_page
│  ├─linux
│  │  └─flutter
│  ├─macos
│  │  ├─Flutter
│  │  ├─Runner
│  │  │  ├─Assets.xcassets
│  │  │  │  └─AppIcon.appiconset
│  │  │  ├─Base.lproj
│  │  │  └─Configs
│  │  ├─Runner.xcodeproj
│  │  │  ├─project.xcworkspace
│  │  │  │  └─xcshareddata
│  │  │  └─xcshareddata
│  │  │      └─xcschemes
│  │  ├─Runner.xcworkspace
│  │  │  └─xcshareddata
│  │  └─RunnerTests
│  ├─test
│  ├─web
│  │  └─icons
│  └─windows
│      ├─flutter
│      └─runner
│          └─resources
├─docs
└─img
```
<br/>

#### 마. 산업체 멘토링 의견 반영사항
&emsp;1 ) 피드백: 사용자 이탈을 막고 신규 사용자를 끌어들일 수 있는 Key Features 추가에 대한 고민이 필요하므로 카카오T, Uber Taxi 등 주요 택시어플을 분석하고 부르릉앱만의 경쟁력이 될 수 있는 기능을 지속적으로 추가할 것을 권장함
  > - 공공 서비스로 제작하여 수수료를 징수하지 않고 수익 그대로를 택시 기사에게 전달함으로서 택시 기사를 끌어들일 수 있는 요소를 추가하였고, 카카오택시, 우버택시에 밀려 어려움을 겪고 있는 지역 운수사와의 제휴를 통해 택시를 공급할 예정임
  > - 부산대학교 학생을 위한 맟춤형 서비스로, 인증 절차를 거친 부산대학교 학생만 이용할 수 있게 함으로서 안전한 택시 이용 환경이라는 Key Feature를 고안하였고, 학생에게 최적화된 어플 사용 환경(시간표를 기반으로 한 목적지 추천) 및 학교 기관 혹은 학생회 등과 협력하여 어플을 홍보하고 사용을 독려할 수 있도록 하여 사용자를 모을 수 있도록 할 예정임. 

&emsp;2 ) 피드백: 택시비 N등분의 경우 배분 과정에 동의 및 서명절차가 필요할 텐데 어느 단계에서 수행할 것인지, 어떤 기술적인 요소가 필요한지 에대한 세부검토를 권장함
  > - 처음에는 선불교통카드와 같이 '부르릉캐시'라 명명한 선불충전형 포인트를 사용하여 결제하려고 하였으나, 최근 발생한 '티몬-위메프 사태'와 같이 어플 및 서비스 신뢰도 면에서 문제가 제기되어 카드나 페이를 결제 수단으로 등록하여 N등분한 금액이 자동결제가 될 수 있도록 결제 방식을 바꾸었음.
  > - 결제 시에는 N등분한 금액을 BRR 서비스의 법인 계좌로 지급받은 후 이를 택시 기사에게 다시 지급하는 방식임
  > - 이때 평균 3 영업일 정도 걸리는 카드결제 대금 지급 기간을 고려하여, 택시 기사에게 택시 요금이 정산되는 날은 3일 뒤로 설정하였음
  > - 더불어 결제 서비스 관련 수수료 등의 운영비는 광고 수익으로 충당할 예정임.

&emsp;3 ) 피드백: 매칭서비스의 경우, 함께 있는 친구를 우선적으로 매칭하는 경우가 자주 필요할 것으로 예상되므로 해당 기능을 포함할 것인지에 검토를 권장함
  > - 친구 추가 기능 및 함께 매칭 서비스의 필요성은 깨달았으나, 개발 단계에서 실현시키지는 못하였음.
  > - 다만 실제로 출시하게 된다면 친구 서비스는 추가할 예정으로, 친구에게 택시 탑승 제안, 채팅 기능, 매칭 초대 기능 등을 추가할 생각임.

&emsp;4 ) 피드백: 개발과정에 5회의 정기회의가 포함되어 있는데 정기회의 시 중간점검/검토/리뷰를 실시할 필요가 있음. 주요 단계별 중간점검을 실시함으로써 최종단계에서의 Fail판정(출시불가) 위험을 예방하기위한 목적임
  > - 5회의 정기회의 이외에도 2, 3일 간격으로 회의하며 서로 간의 프로젝트 이해도를 높였고, 회의 진행 시 프론트엔드, 백엔드 각 부문 진행상황을 보고한 후 해당 내용에 대한 검토를 진행하였고 추후 개발 일정과 기능 등에 대하여 토의하였음.
  > - 더불어 각 부문에서 필요하거나 필요하다고 생각하는 부분을 자유롭게 논의하며 프로젝트 전체의 완성도를 향상시켰음.

### 4. 설치 및 사용 방법
> 제품을 설치하기 위헤 필요한 소프트웨어 및 설치 방법을 작성하세요.

```
$ git clone https://github.com/pnusw-hackathon/PNUSW-2024-team-12.git  
$ cd PNUSW-2024-team-12/brr                                   
$ flutter pub get                                                     
$ flutter run
```

### 5. 소개 및 시연 영상
> 프로젝트에 대한 소개와 시연 영상을 넣으세요.

순서대로 매칭 방을 만드는 사용자, 택시기사, 매칭에 참여하는 타 사용자


https://youtu.be/cT4UYSdCUgM

### 6. 팀 소개
> 팀원 소개 & 구성원 별 역할 분담 & 간단한 연락처를 작성하세요.

| 권민준 | 김태우 | 김효정 | 안선주 | 이지헌 | 정희철 |
|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
| <img width="80px" alt="MEMBER3" src="/img/권민준.png" /> | <img width="80px" alt="MEMBER3" src="/img/김태우.png" /> | <img width="80px" alt="MEMBER3" src="/img/김효정.png" /> | <img width="80px" alt="MEMBER3" src="/img/안선주.png" /> | <img width="80px" alt="MEMBER3" src="/img/이지헌.png" /> | <img width="80px" alt="MEMBER3" src="/img/정희철.png" /> |
| mjiun13@pusan.ac.kr | minecoby@pusan.ac.kr | hyojeong0109@pusan.ac.kr | pusanju83@pusan.ac.kr | leejiheon0516@pusan.ac.kr | gmlcjf0419@pusan.ac.kr |
| 디자이너 | 인프라 구축 <br/> 백앤드 개발 | 팀장 <br/> 프론트앤드 개발 | 디자이너 | 디자이너 <br/> 프론트앤드 개발 | DB 설계 <br/> 백앤드 개발 |
### 7. 해커톤 참여 후기
> 팀원 별 해커톤 참여 후기를 작성하세요.

- 권민준
  > 처음 도전해보는 해커톤이라 시작할 때는 많은 걱정을 했지만 다행히 좋은 팀원들과 함께하여 즐겁게 진행 할 수 있었습니다. 또한 앱의 ux/ui 디자인과 관련하여 작업물을 만들면서 디자인적으로 더 발전 할 수 있었고, 평소에 잘 모르던 개발 분야를 팀원들의 도움으로 잘 이해하는 계기가 되었습니다. 팀원들과 소통하며 해커톤을 진행해가는 과정에서 열심히 맡은 일을 하는 팀원들을 보며 저 역시 어떠한 일을 하는 원동력을 얻을 수 있어 좋았습니다

- 김태우
  > 이번 해커톤에서 FastAPI를 사용해 백엔드 개발을 진행하며, 이전에 공부하던 내용을 실전에 적용하고 실력을 더욱 향상시킬 수 있었습니다. 특히, 빠른 속도의 API 개발과 효율적인 데이터 처리 방법을 직접 구현하며 FastAPI의 강점을 체감할 수 있었습니다. 백엔드뿐만 아니라, 디자이너와 프론트엔드 개발자 등 다양한 직군의 팀원들과 협업하는 과정을 통해, 각자의 역할이 얼마나 중요한지 다시금 깨닫게 되었습니다. 단순한 코드 작성이 아닌, 전체적인 시스템의 일부분을 담당하는 책임감과 협력의 중요성을 느낄 수 있었습니다. 또한, 빠른 의사소통과 명확한 역할 분배가 프로젝트 완성도를 높이는 핵심이라는 것을 경험하며, 협력하는 개발의 재미를 크게 느꼈습니다. 이번 해커톤을 통해 팀워크와 기술적 역량 모두에서 큰 성장을 이룰 수 있었고, 이후 진행될 다른 해커톤에도 참여하여, 저의 역량을 더욱더 키워나갈 것입니다.

- 김효정
  > 입학 전 SW 중심대학 주관 해커톤 이후, 처음으로 해커톤에 참여하게 되어 걱정과 설렘이 함께하였습니다. 작년부터 배워온 Flutter를 활용하여 앱을 제작하였고 이전에 두 번의 프로젝트를 진행하면서 매번 Flutter에 대하여 배워왔기에 이번 해커톤에서 UI구성 뿐만 아니라 백엔드 연결에 조금 더 수월하게 진행 할 수 있었습니다. 디자인을 맡아준 팀원 들 덕분에 UI 구성에서 막힘 없이 코드를 작성 할 수 있었고, 팀원 모두가 진행, 기획 등 많은 부분을 도와주어 조장 이라는 역할을 부담없이 할 수 있었습니다. 또한 2달이라는 시간을 팀원들과 함께 작업하면서, 과연 제대로 구현 할 수 있을 까 라는 막막함도 있었지만 결과물이 꽤나 완성적이라서 뿌듯하였습니다. 

- 안선주
  > 앱 개발을 처음부터 끝까지 디자인하고, 개발팀에게 넘겨주는 과정까지 진행해보니 얻은 것이 정말 많았습니다. 첫 번째로, 디자인할 때 중요하게 생각해야 하는 것이 무엇인지 더 자세히 알아가고 관심을 가지게 되었습니다. 디자인 학과에서 수업시간에 배우는 것들은 사용자의 입장에서 생각하려고 해도 일단 디자인이 예쁘게 나오는 것이 중요하다고 생각했는데, 실제 앱을 만들다 보니 사용자를 유도하도록 만드는 디자인에 좀 더 집중하게 되었습니다. 두 번째로, 개발 과정을 좀 더 자세히 알 수 있었습니다. 우리 팀은 매주 회의를 하며 개발 진행 상황과 디자인 진행 상황을 공유했는데, 매주 어떻게 개발되는지, 어떤 부분의 구현이 왜 어려운지 등을 알게 되어서 신기하기도 했고, 전혀 몰랐던 개발 관련 지식이 조금씩 쌓이는 느낌이 들었습니다. 마지막으로, 프로젝트를 진행해 나가는 과정을 배웠습니다. 대학 생활을 하면서 겪었던 프로젝트는 거의 개인 프로젝트였는데, 다 같이 진행하는 이런 프로젝트에서 회의 방식이나 과정을 확실히 배운 것 같습니다. 많은 것을 얻은 활동이어서 참여가 더욱 흥미로웠고, 따로 또 다른 앱을 출시해보고 싶다는 생각도 들었습니다.

- 이지헌
  > 저라는 사람의 부족함을 여실히 깨달은 경험이었습니다. 이번 해커톤 대회서 명목상으로는 프론트엔드 개발을 맡았고, 디자인과 기획에도 일정 부분 기여하기는 했으나, 마지막에 돌아보니 제대로 한 게 없는, 결국은 흔히 말하는 '버스를 탄' 모양새가 되었습니다. C나 Python등의 기초 정도는 배운 적이 있지만, 이런 프로젝트를 해본 경험도, 실력도 모자란 상황이었습니다. 이런 상황에서. 물론 제 불성실함도 가장 큰 원인이었겠지만, 프론트엔드 개발을 아예 처음 시도해보는지라 어려움도 많았고, 결과물에 비해 소요되는 시간도 너무나 많았습니다. 결국 대부분의 작업은 프론트엔드 개발을 맡은 다른 팀원분이 진행하게 되었고, 저는 그분에게 많은 부담을 안겨주게 되었습니다. 팀이 구성되었던 대회 초반에, 당당히 프론트엔드를 해보겠다고 한 제 자신의 오만함이 얼마나 부끄러운지 모르겠습니다. 다행히도 좋은 팀원들을 만나 어떻게 프로젝트를 잘 마무리하긴 했지만, 욕심과 의욕만 앞서 다른 팀원들에게 짐만 안겨준 셈이 되어버렸으니 굉장히 미안하고 고마운 마음입니다. 만약에 다음에도 이처럼 프로젝트 단위의 일을 하게 된다면 저 자신이 어떤 역량을 보유하고 있는지 객관적으로 돌아보고, 할 수 있는 범위 내에서 최선을 다하는 사람이 되었으면 합니다.

- 정희철
  > SW 중심대학의 프로그램에 입학부터 꾸준히 참여했습니다. 참여할 때마다 개발 실력이 향상되는 것을 느꼈지만, 이번 해커톤을 통해 더 큰 폭의 실력 향상을 체감했습니다. 담당 업무는 백엔드였지만, 이전에는 백엔드를 거의 접해보지 못해 어디서부터 시작해야 할지 몰랐습니다. 무작정 공부하면서 동시에 개발을 진행했습니다. 6월에 작성한 코드를 보면 수정하고 싶은 부분이 많을 정도입니다. 해커톤을 진행하며 많은 오류를 만났고, 이를 해결하는 과정에서 성장했기에 SW 해커톤에 참여한 것이 매우 뿌듯합니다.





