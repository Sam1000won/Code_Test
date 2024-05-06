# [Bronze I] 전주 듣고 노래 맞히기 - 31562 

[문제 링크](https://www.acmicpc.net/problem/31562) 

### 성능 요약

메모리: 31120 KB, 시간: 292 ms

### 분류

브루트포스 알고리즘, 자료 구조, 해시를 사용한 집합과 맵, 구현, 문자열

### 제출 일자

2024년 5월 6일 14:59:21

### 문제 설명

<p>윤수와 정환은 「전주 듣고 노래 맞히기」라는 게임을 할 예정이다. 「전주 듣고 노래 맞히기」는 주어진 노래의 전주를 듣고 먼저 제목을 맞히는 사람이 점수를 얻어 최종적으로 점수가 더 많은 사람이 이기는 게임이다. 절대 음감을 가진 윤수는 노래의 첫 네 음만 듣고도 어떤 노래든 바로 맞힐 수 있다. 따라서, 정환은 윤수를 이기기 위해 첫 세 음만으로 노래를 맞히게 해주는 프로그램을 만들려고 한다. 우선 정환이 알고 있는 노래 제목, 음이름 등을 데이터로 만든 뒤 프로그램을 구현하기 시작했다. 예를 들어, 다음은 <span style="color:#e74c3c;"><code>TwinkleStar</code></span>(반짝반짝 작은 별)의 악보 중 일부이다.</p>

<p style="text-align: center;"><code><img alt="" src="" style="height: 137px; width: 594px;"></code></p>

<p>위 악보를 박자와 관계없이 음이름으로 표현하면 <span style="color:#e74c3c;"><code>CCGGAAG</code></span>가 된다.</p>

<p>윤수를 이기기 위해서는 이 프로그램이 첫 세 음인 <code><span style="color:#e74c3c;">CCG</span></code>만으로 노래 제목인 <span style="color:#e74c3c;"><code>TwinkleStar</code></span>를 출력할 수 있어야 한다. 또한, 세상의 모든 노래를 아는 윤수와 다르게 정환은 음을 아는 노래가 $N$개뿐이다. 그래서 프로그램에 $N$개의 노래의 정보를 저장해 놓을 것이다. 만약 저장된 노래 중 입력한 첫 세 음으로 시작하는 노래가 여러 개 있어 무슨 노래인지 정확히 알 수 없는 경우 <span style="color:#e74c3c;"><code>?</code></span>를 출력하고, 입력한 첫 세 음에 맞는 저장된 노래가 없을 경우 <span style="color:#e74c3c;"><code>!</code></span>를 출력한다.</p>

<p>정환을 도와서 첫 세 음만으로 본인이 음을 아는 노래를 맞히는 프로그램을 완성하자. 이 프로그램은 대문자와 소문자를 구분한다.</p>

### 입력 

 <p>첫 번째 줄에 정환이 음을 아는 노래의 개수 $N$, 정환이 맞히기를 시도할 노래의 개수 $M$이 공백으로 구분되어 주어진다.</p>

<p>두 번째 줄부터 $N$개의 줄에 걸쳐 노래 제목의 길이 $T$, 영어 대소문자로 이루어진 문자열 노래 제목 $S$, 해당 노래에서 처음 등장하는 일곱 개의 음이름 $a_1, a_2, a_3, a_4, a_5, a_6, a_7$이 공백으로 구분되어 주어진다.</p>

<p>$N+2$번째 줄부터 $M$개의 줄에 걸쳐 정환이 맞히기를 시도할 노래의 첫 세 음의 음이름 $b_1, b_2, b_3$가 공백으로 구분되어 주어진다.</p>

<p>주어지는 음이름은 각각 <code><span style="color:#e74c3c;">C</span></code>, <code><span style="color:#e74c3c;">D</span></code>, <code><span style="color:#e74c3c;">E</span></code>, <code><span style="color:#e74c3c;">F</span></code>, <code><span style="color:#e74c3c;">G</span></code>, <code><span style="color:#e74c3c;">A</span></code>, <code><span style="color:#e74c3c;">B</span></code> 중 하나이다. 같은 제목이 두 번 이상 주어지지 않는다.</p>

### 출력 

 <p>정환이 맞히기를 시도할 각 노래에 대하여 프로그램에 저장된 노래와 첫 세 음이 동일한 노래가 하나만 있다면 해당 노래의 제목을, 두 개 이상이면 <code><span style="color:#e74c3c;">?</span></code>을, 없다면 <code><span style="color:#e74c3c;">!</span></code>을 한 줄에 하나씩 출력한다.</p>

