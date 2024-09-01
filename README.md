
### 1. 프로젝트 소개
#### 가. 개발배경 및 필요성
- 현재 부산대학교 순환버스(금정7번)은 등교 시간대에 그 수요를 공급이 따라가지 못하고 있다. 등교 시간대에 부산대역에는 09시 수업을 듣기 위해 최대 80명까지 대기 줄이 형성되어있으며, 이뿐만 아니라 부산대학교 정문에서 순환버스를 탑승하려고 해도, 이미 탑승자가 너무 많아 탑승하지 못하는 문제가 빈번하게 발생한다. 이로 인해 지각을 하게 되는 경우도 잦다. 실제로 09시 이후에도 순환버스는 사람이 들어갈 자리가 없을 정도로 그 밀집도가 높다.

- 이로 인해 버스를 탑승하지 않고 택시를 타는 경우가 발생한다. 혼자서 택시를 탈 경우 기본요금 4800원부터 시작하여 금액이 상승하며, 부산대역에서 부산대학교 내의 경영관까지 가는데 필요한 금액이 4800원으로, 버스요금 1400원보다 경제적 부담이 생긴다.

- 수요가 많다보니 순환버스가 안전하게 수용할 수 있는 최대 인원을 넘어서 타는 일이 부지기수며, 사람이 탑승하면 위험한 버스 출입구에 사람이 서 있는 위험한 경우도 심심찮게 볼 수 있다. 

- 또한 밤늦게 귀가할 때, 막차 시간을 놓친 학생들은 부득이하게 택시를 탈 수 밖에 없으며, 남자 기숙사에 사는 원생의 경우 우리 대학에서 가장 높은 건물 중 하나인 웅비관 혹은 진리관까지 걸어가야하는 상황이 발생한다. 이때 거리와 심야할증을 고려하면 경제적 부담이 만만치 않다. 

- 이에 순환버스가 수요를 따라가지 못하는 상황에서 순환버스를 대체할 다른 이동수단이 학생들에게 필요하다는 문제에서 공유 택시 서비스라는 아이디어를 도출하였다. 

- 더불어 그 범위를 확장해, 우리 대학에 다양한 지역에서 등하교하는 학생들이 술자리 이후 밤 늦게 집에 가는 학생들 역시 좀 더 값싼 가격에 안전하게 귀가할 수 있도록 비슷한 목적지를 가진 학생들끼리 택시를 공유할 수 있는 서비스를 창안해내게 되었다.


#### 나. 개발 목표 및 주요 내용
 ○ 개발목표
- 첫 번째 목표는 부산대학교 순환버스의 공급 부족 문제를 해결하여 교통 혼잡을 완화하고, 학생들이 시간에 맞춰 강의실에 도착할 수 있도록 지원하는 것이다 또한, 택시 공유 시스템을 통해 학생들의 교통비를 절감하고, 특히 야간 및 심야 시간대에 저렴한 비용으로 안전하게 이동할 수 있도록 한다. 
- 순환버스의 과밀로 인한 안전 문제를 해결하고, 쾌적하고 안전한 교통 환경을 조성하고, 더불어 막차 시간을 놓친 학생들이 안전하고 경제적으로 귀가할 수 있도록 택시 공유 시스템을 개발하여 지원하고자 한다. 
- 공유 택시 서비스를 도입하여 교통 혼잡을 줄이고, 탄소 배출량을 감소시켜 환경 보호에 기여하며, 교통 자원을 효율적으로 배분하여 학생들의 다양한 이동 수요를 충족시키는 것을 목표로 한다. 
- 마지막으로, 부산대학교와 주변 지역 사회 간의 교통 협력을 강화하여 학생들의 이동 편의성을 높이고, 지역 경제 활성화에 기여하도록 한다.

 ○ 주요내용
- 공유 택시 서비스는 유저들이 택시를 타고 가고자 하는 출발지와 목적지를 앱에 등록하면, 출발지와 목적지가 비슷한 유저들을 매칭하여 함께 택시를 탈 수 있는 서비스이다. 이를 통해 유저들은 택시 비용을 절감하고, 보다 편리하게 이동할 수 있다. 
- 가격 책정은 최종 목적지에 도착했을 경우 택시 미터기의 금액으로 계산하도록한다. 모바일 결제를 통해 간편한 결제를 지원하는 시스템을 도입한다. 
- 특히 해당 서비스는 부산대학교 학생을 대상으로 지원한다. .

#### 다. 세부내용
 ○ 요구사항 분석 (사용자 및 기능요구사항)*
  가. 유저 기능

1) 택시 호출 기능
  - 홈페이지(#0)에서 빠른매칭 또는 예약매칭 버튼을 클릭하면 택시 호출을 할 수 있다.

2) 매칭 서비스
  - 출발지가 비슷한 위치의 유저들이, 목적지가 같거나, 목적지를 가는 길목에 하차를 할 경우 택시를 함께 탈 수 있도록 매칭해주는 서비스이다.
  - 매칭 시 희망 인원을 선택할 수 있다.
  - 매칭 방식은 빠른 매칭(#1) / 예약 매칭(#2, #3)으로 나뉜다.

  - 빠른 매칭(#1) : 근처에 있는 사람들 중 목적지가 비슷한 위치의 사용자들을 바로 매칭해주는 서비스이다.
  - 예약 매칭(#2, #3): 출발지, 목적지, 탑승 시간, 모집 인원 등이 포함된 글을 올려 매칭을 예약해주는 서비스이다. 예를 들면 “”“출발지 : 부산대역, 목적지 : 경암체육관, 탑승시간 13시 00분, 모집인원 3명”“” 이렇게 정보가 있는 예약페이지를 통해 탑승 모집 예약을 할 수 있다. 그 후 예약된 탑승시간에 택시를 호출하게 한다.
  - 매칭이 진행 중일 때는 매칭 대기 페이지(#4)에서 대기하며, 출발해요버튼을 클릭한 경우 모달창을 통해 매칭된 인원들에게 출발 여부를 확인한다.
  - 일반 사용자는 매칭 목록 페이지(#7)을 통해 현재 모집 중인 빠른 매칭과 예약매칭 목록을 확인할 수 있고, 클릭할 경우 매칭대기 페이지(#4)로 이동할 수 있다. 
  - 매칭이 완료되면 알림을 통해 매칭 완료여부를 알려준다. 
  - 매칭 알고리즘의 우선순위는 출발위치, 도착위치 순서이다.

#2 예약매칭
  - 매칭이 다 된 후 택시 호출을 시작하면, 현재 택시의 위치와 나의 위치가 보이는 택시호출화면(#5)을 보여준다.
  - 홈페이지(#0)에서 나의 예약목록을 볼 수 있다.

3) 매칭 커뮤니티
  - 출발지로 모이기 위해 매칭된 유저들끼리 소통할 수 있도록 채팅방(#6)를 구성한다.
  - 해당 커뮤니티는 택시 하차 후 자동 삭제된다. 

4) 매칭 목록 페이지(#7)
  - 사용자는 택시호출을 직접하지 않아도 매칭 목록 페이지를 들어가 예약된 택시 목록을 볼 수 있다.
  - 목록을 클릭하면 매칭이 되고, 매칭대기페이지(#4)로 이동한다.
  - 매칭 목록 페이지에는 빠른매칭과 예약매칭을 둘 다 볼 수 있다.
  - 목록을 보여주는 우선순위는 예약된 탑승시간(빠른매칭일 경우 호출시간과 탑승시간 같다고 판단)을 기준으로 현재시간에서 가장 근접한 탑승시간 순서로 보여준다. 
  - 출발지 또는 목적지를 검색했을 경우, 검색 조건에 맞는 상황에서 탑승시간 순서로 리스트를 보여준다. 
  - 매칭 목록에는 출발지, 목적지, 탑승시간등의 정보들을 보여준다.

5) 자동결제 서비스 
  - 매칭이 확정된 후 택시에서 하차하면 금액을 N등분 한 가격을 각자 택시기사에게 자동 결제한다.
  - 자동결제 시스템은 카카오페이 API를 사용할 계획이다. 

6) 시간표 등록(#9) 
  - 부르릉은 부산대생에 한정하여 배포할 예정이다. 이에 따라 시간표를 등록하면 홈페이지(#0)에서 어느 건물로 가야하는지 자동으로 볼 수 있다. 
  - 사용자끼리 도착지 건물의 위치가 비슷하면 비슷한 사람들끼리 자동 매칭이 가능하다.

7) 본인확인 
  - 회원가입은 학번과 비밀번호를 통해 진행한다. 
  - 학생증 사진을 첨부하여 소속인증을 진행한다. 
  - 전화번호 인증을 한다. 

8) 마이페이지(#8)
  - 개인정보 관리 : 아이디와 비밀번호를 관리할 수 있다. 
  - 시간표 관리 : 시간표를 등록하고 관리할 수 있다.(#9)
  - 계좌 관리 : 결제를 할 카드를 등록할 수 있다. 
  - 이용기록 : 탑승시간, 하차시간, 금액, 출발지, 목적지 등 부르릉 사용에 관련된 이용기록이 있다.

9) 로그인 및 회원가입(#10, #11)
  - 부르릉을 사용하기 위해서는 회원가입이 필요하다.
  - 회원가입을 할 때 사용자인지 택시기사인지 선택을 해야한다.
  - 회원가입 정보는 이름, 아이디, 비밀번호, 학번, 전화번호 등으로 구성되어 있다.
 
나. 택시 기사 기능
1) 호출 받기 
  - 회원가입을 할 때 택시기사라고 선택했을 경우 이 기능이 추가된다.
  - 택시기사는 택시기사의 전용페이지(#12)와 콜대기 및 콜수락 페이지(#13, #14)을 통해 호출을 받을 수 있다.
  - 택시기사 전용 마이페이지(#15)를 통해 기사정보를 관리할 수 있다.


#### 라. 기존 서비스 대비 차별성
기존의 Kakao Taxi 등 타 회사의 택시호출 어플에는 공유택시 기능이 없다. 부르릉은 공유택시기능을 추가하여 사용자(부산대생을 한정)의 경제적 부담을 줄이고, 순환버스 과밀로 인한 위험성을 방지한다. 이를 통해 쾌적한 학교생활을 돕도록 한다. 또한 매칭 예약을 통해 탑승하고자하는 시간에 택시를 호출해주는 기능을 추가하였다.  

#### 마. 사회적가치 도입 계획
1) 안전한 교통 환경 조성
  - 교통 혼잡 완화: ‘부르릉’ 서비스는 부산대학교 순환버스의 수요 과잉 문제를 해결하여 교통 혼잡을 줄이고, 학생들이 안전하게 교내를 이동할 수 있도록 합니다. 과밀로 인한 사고 위험을 줄이며, 보다 안전하고 쾌적한 교통 환경을 제공합니다.
  - 야간 이동 안전 보장: 늦은 시간에 택시를 이용해야 하는 학생들이 안전하게 귀가할 수 있도록 도와줍니다. 특히 여학생이나 밤 늦게 귀가하는 학생들에게 택시 공유 서비스는 안전한 이동 수단을 제공합니다.

2) 경제적 부담 경감
  - 교통비 절감: 순환버스의 부족으로 인해 택시를 이용해야 하는 학생들의 경제적 부담을 덜어줍니다. 공유 택시 서비스를 통해 택시 요금을 분담함으로써 개별적으로 택시를 이용할 때보다 훨씬 저렴한 비용으로 이동할 수 있습니다.
  - 환경 보호 기여: 공유 택시 서비스를 통해 탄소 배출량을 줄여 환경 보호에 기여합니다. 이는 학생들이 대중교통을 더욱 효율적으로 이용하게 함으로써 교통 자원의 낭비를 줄이는 효과도 있습니다.

3) 지역 사회와의 협력 강화
  - 지역 경제 활성화: 부산대학교와 주변 지역 사회 간의 교통 협력을 강화하여 지역 경제 활성화에 기여합니다. 택시 기사들과의 협력을 통해 지역 경제에 긍정적인 영향을 미치며, 더 나아가 지역 내 교통 서비스의 질을 높이는 데 기여할 수 있습니다.
  - 교통 자원 효율적 배분: 학생들의 다양한 이동 수요를 충족시키기 위해 교통 자원을 효율적으로 배분합니다. 이는 지역 내 교통 체계의 전반적인 개선에도 긍정적인 영향을 미칩니다.

4) 편리하고 신뢰할 수 있는 서비스 제공
  - 편리한 매칭 시스템: 출발지와 목적지가 비슷한 사용자들을 매칭하여 택시를 함께 이용할 수 있도록 지원합니다. 이는 학생들이 보다 편리하게 택시를 이용할 수 있도록 하며, 시간과 비용을 절약하는 데 도움을 줍니다.
  - 안전한 결제 시스템: 모바일 결제 시스템을 통해 간편하고 안전한 결제를 지원합니다. 자동 결제 시스템을 도입하여 결제 과정의 번거로움을 줄이고, 사용자들의 편의성을 높입니다.

5) 학생 복지 향상
  - 시간표 기반 매칭: 학생들이 시간표를 등록하여 보다 효율적으로 택시를 이용할 수 있도록 합니다. 도착지 건물의 위치가 비슷한 학생들끼리 자동 매칭을 통해 편리한 이동을 지원합니다.
  - 본인 인증 시스템: 회원가입 시 학번과 학생증 사진, 전화번호 인증을 통해 신뢰할 수 있는 사용자만 이용할 수 있도록 하여 서비스의 안전성을 높입니다.


### 2. 상세설계
#### 가. 시스템 구성도



#### 나. 사용 기술
> 스택 별(backend, frontend, designer등) 사용한 기술 및 버전을 작성하세요.
> 
> ex) React.Js - React14, Node.js - v20.0.2

### 3. 개발결과
#### 가. 전체시스템 흐름도
1) IA(Information Architecture)
2) 유저 플로우 차트
   
   2-1) 유저 전체 플로우 차트
   > 회원의 전체 플로우 차트입니다.
   
   <img src="/docs/brr 유저 전체 페이지.jpg" width="800px" title="유저 전체 플로우 차트" alt="Alt text"></img>

   

   2-2) 회원가입 플로우 차트
   > 회원가입 플로우 차트입니다.
   
   <img src="/docs/회원가입 플로우 차트.jpg" width="800px" title="유저 전체 플로우 차트" alt="Alt text"></img>

   2-3) 기사 전체 플로우 차트
   > 택시기사의 전체 플로우 차트입니다.
   
   <img src="/docs/brr 기사 전체 페이지.jpg" width="600px" title="기사 전체 플로우 차트" alt="Alt text"></img>
   
2) 테스크 플로우 차트
 
   3-1) 로그인 및 회원가입 플로우 차트
   > 로그인과 회원가입의 플로우 차트입니다.

    회원가입 시 유저는 회원(손님)과 택시기사로 나뉩니다.
   
    회원은 아이디, 비밀번호, 이름, 전화번호, 학번, 이메일의 정보를 입력합니다.
   
    택시기사는 아이디, 비밀번호, 이름, 전호번호, 자동차 번호, 자동차 모델을 입력합니다.

    로그인 시 회원일 경우 회원페이지로, 택시기사의 경우 택시기사 페이지로 이동합니다.
   <img src="/docs/로그인 및 회원가입 플로우차트.jpg" width="800px" title="Title" alt="Alt text"></img>
 
3) 시스템 플로우 차트
 
   4-1) 이메일 인증 플로우 차트
   > 이메일 인증 플로우 차트입니다.
   
   <img src="/docs/brr 이메일 인증 플로우 차트.jpg" width="800px" title="Title" alt="Alt text"></img>
   
   4-2) 매칭 플로우 차트
   > 매칭 플로우 차트입니다.
   
   <img src="/docs/brr 매칭 플로우차트.jpg" width="800px" title="Title" alt="Alt text"></img>
   
4) ERD

   5-1) database ERD
   > BRR 전체 database ERD입니다. 
   
   <img src="/docs/brr ERD.jpg" width="800px" title="Title" alt="Alt text"></img>






#### 나. 기능설명
> 각 페이지 마다 사용자의 입력의 종류와 입력에 따른 결과 설명 및 시연 영상.
> 
> ex. 로그인 페이지:
> 
> - 이메일 주소와 비밀번호를 입력하면 입력창에서 유효성 검사가 진행됩니다.
> 
> - 요효성 검사를 통과하지 못한 경우, 각 경고 문구가 입력창 하단에 표시됩니다.
>   
> - 유효성 검사를 통과한 경우, 로그인 버튼이 활성화 됩니다.
>   
> - 로그인 버튼을 클릭 시, 입력한 이메일 주소와 비밀번호에 대한 계정이 있는지 확인합니다.
>   
> - 계정이 없는 경우, 경고문구가 나타납니다.
>
> (영상)

#### 다. 기능명세서
> 개발한 제품에 대한 기능명세서를 작성해 제출하세요.
> 
> 노션 링크, 한글 문서, pdf 파일, 구글 스프레드 시트 등...

#### 라. 디렉토리 구조
> 위 레포지토리의 디렉토리 구조를 설명하세요.

#### 마. 산업체 멘토링 의견 반영사항


### 4. 설치 및 사용 방법
> 제품을 설치하기 위헤 필요한 소프트웨어 및 설치 방법을 작성하세요.
>
> 제품을 설치하고 난 후, 실행 할 수 있는 방법을 작성하세요.

### 5. 소개 및 시연 영상
> 프로젝트에 대한 소개와 시연 영상을 넣으세요.
> 프로젝트 소개 동영상을 교육원 메일(swedu@pusan.ac.kr)로 제출 이후 센터에서 부여받은 youtube URL주소를 넣으세요.

### 6. 팀 소개
> 팀원 소개 & 구성원 별 역할 분담 & 간단한 연락처를 작성하세요.

### 7. 해커톤 참여 후기
> 팀원 별 해커톤 참여 후기를 작성하세요.

<br/>


## 4. README.md 작성 팁
- 마크다운 언어를 이용해 README.md 파일을 작성할 때 참고할 수 있는 마크다운 언어 문법을 공유합니다.
- 다양한 예제와 보다 자세한 문법은 [이 문서](https://www.markdownguide.org/basic-syntax/)를 참고하세요.

### 4.1. 헤더 Header
```
# This is a Header 1
## This is a Header 2
### This is a Header 3
#### This is a Header 4
##### This is a Header 5
###### This is a Header 6
####### This is a Header 7 은 지원되지 않습니다.
```

# This is a Header 1
## This is a Header 2
### This is a Header 3
#### This is a Header 4
##### This is a Header 5
###### This is a Header 6
####### This is a Header 7 은 지원되지 않습니다.
<br />

### 4.2. 인용문 BlockQuote
```
> This is a first blockqute.
>	> This is a second blockqute.
>	>	> This is a third blockqute.
```
> This is a first blockqute.
>	> This is a second blockqute.
>	>	> This is a third blockqute.
<br />

### 4.3. 목록 List
* **Ordered List**
```
1. first
2. second
3. third  
```
1. first
2. second
3. third
<br />

* **Unordered List**
```
* 하나
  * 둘

+ 하나
  + 둘

- 하나
  - 둘
```
* 하나
  * 둘

+ 하나
  + 둘

- 하나
  - 둘
<br />

### 4.4. 코드 CodeBlock
* 코드 블럭 이용 '``'
```
여러줄 주석 "```" 이용
"```
#include <stdio.h>
int main(void){
  printf("Hello world!");
  return 0;
}
```"

단어 주석 "`" 이용
"`Hello world`"

* 큰 따움표(") 없이 사용하세요.
``` 
<br />

### 4.5. 링크 Link
```
[Title](link)
[부산대 소프트웨어융합교육원](https://swedu.pusan.ac.kr/swedu/index.do)

<link>
<https://swedu.pusan.ac.kr>
``` 
[부산대 소프트웨어융합교육원](https://swedu.pusan.ac.kr)

<https://swedu.pusan.ac.kr>  
<br />

### 4.6. 강조 Highlighting
```
*single asterisks*
_single underscores_
**double asterisks**
__double underscores__
~~cancelline~~
```
*single asterisks* <br />
_single underscores_ <br />
**double asterisks** <br />
__double underscores__ <br />
~~cancelline~~  <br />
<br />

### 4.7. 이미지 Image
```
<img src="/path/to/img.jpg" width="600px" title="Title" alt="Alt text"></img>
![Alt text](/path/to/img.jpg "Optional title")
```
<img src="https://github.com/pnuswedu/SW-Hackathon-2024/assets/34933690/be7beb64-490f-4480-b121-f25cde7f2a8d" width="600px" title="부산대학교 소프트웨어융합교육원" alt="부산대학교 소프트웨어융합교육원"></img>
<br/>
![부산대학교 소프트웨어융합교육원](https://github.com/pnuswedu/SW-Hackathon-2024/assets/34933690/884154bb-28f6-4498-9f64-a8a878972951, "부산대학교 소프트웨어융합교육원")
<br/>

















