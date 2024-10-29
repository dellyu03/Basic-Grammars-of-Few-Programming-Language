# Input (for Python CodingTest)
> 파이썬 코딩 테스트 관련 입력 기법 정리

## Input 사용
> 가장 기본적인 사용 방법

[기본 입력](../../../Bassic-Programming-Syntaxes/Python/Input-Output.md) 사용 방법

## 1. Python에서 Input 동작 원리
1. 입력 대기
    - 사용자 입력을 기다리는 상태
2. 입력 내용 수집
    - 각 문자를 입력 버퍼에 저장
    - 제어(backspace, Enter) 처리를 기다림
3. 입력 버퍼의 내용 처리
    - 버퍼에서 문자열 생성
4. 반환값 생성
    - 버퍼의 내용을 input함수로 반환값

## 2. 장점
- 간편하고 직관적이다.
- 시간제한이 없는 문제에서는 초보자가 가볍게 사용할 수 있다.
### 3. 단점
- #### 입력 속도 
    - 사용자 입력을 한글자 한글자 기다리기 때문에 입력 자체의 속도가 느리다.
- #### 문자열 처리 
    - 사용자가 입력을 문자열로 변환시키는 과정이 존재한다.
- #### 여러줄 입력 처리 
    - 여러줄의 입력을 처리하는 경우 줄마다 새로 호출해야 함

##  3. 사용 요령
- map과 split과 함께 사용해서 여러개의 변수에 한꺼번에 특정 함수를 적용한 사용자 입력을 받을 수 있음
(참조: [map](), [string-자주 쓰는 문자열 함수-split](../../../Bassic-Programming-Syntaxes/Python/Data-Type/String.md))
```Python
userInput1, userInputB = map(int, input().split()) 
```
