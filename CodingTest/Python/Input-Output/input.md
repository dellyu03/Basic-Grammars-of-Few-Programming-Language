# Input (for Python CodingTest)
> 파이썬 코딩 테스트 관련 입력 기법 정리

# I. Input 사용
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

<br>

# II sys.stdin.readline
> sys 객체를 사용한 방법

> sys 객체 - 파이썬 프로그램과 운영체제 간의 상호작용을 도와주는 객체

```python
import sys
n = int(sys.stdin.readline().strip())
```

## 1. sys.stdin.readline 작동원리
- ### 입력 대기
    - 메서드 호출 후 데이터를 기다림
- ### 한줄 입력 받음
    - 한줄 전체를 한꺼번에 입력받음 (개행 문자까지 포함)
    - strip() 함수를통해 제거해야 함
- ### 버퍼에 저장 
    - 입력 데이터를 버퍼에 저장 해둠

- ### 종료 신호 받고 반환
    - EOF 신호가 오기 전까지 계속 입력을 받음
    - EOF 도달 하면 빈 문자열을 반환하며 종료

## 2. 장점 
- ### 대용량 입력 빠른 입력 처리
    - input과는 달리 줄 단위로 입력받오 대용량 데이터 처리에 유리

## 3. 단점
- ### 개행문자 포함
- ### 모듈 임포트 필요
- ### 단일 입력 비효율적



## readlines
> 줄 단위로 여러 줄을 한번에 읽어와 리스트로 리턴함

```python
Hello
World
Python
```

```python
import sys

lines = sys.stdin.readlines()

# lines = [line.strip() for line in lines] 개행 문자 제거 코드
```
리턴값
```python
['Hello\n', 'World\n', 'Pythonn\n']
```

## sys.stdin
> 

