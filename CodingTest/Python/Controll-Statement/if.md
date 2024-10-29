# If (for Python Coding-Test)

## [If 기본 사용법](../../../Bassic-Programming-Syntaxes/Python/Control-Statements/if.md)

## I. 코딩 테스트용 If 사용 기법

- ### 삼항 조건 연산자와 인덱스 유연성 사용 (1330번)
```python
print("==" if A == B else "><"[A < B])
print(['><'[a<b],'=='][a==b])
```
인덱스에 조건문이 들어가도 참이면 1 거짓이면 0을 리턴하는 걸 이용해서 문자열 인덱스의 0번째 1번째 인덱스 리턴을 하게 해 메모리를 줄임 속도는 더 느리더라...

<br>

- ### 필수조건, 필요조건, 충분조건의 활용(2753번)
```python
year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(1)
else:
    print(0)

```
왼쪽 조건이 참이 아니면 true가 나올 수 없지만 or 연산자에 의해 오른쪽 항에 대한 불필요한 연산이 진행됨


```python
year = int(input())

if n % 4 == 0 and (n % 100 != 0 or n % 400 == 0):
    print(1)
else:
    print(0)

```
조건에 따른 불필요한 연산이 줄어들어 속도가 약간 향상됨
- 충분 조건을 먼저 연산하게 하여 속도를 줄인다.
- 단축평가(충분조건이 충족되면 결과를 반환)를 고려하여 코드를 짜자 
- or에서 먼저 계산된쪽이 참이면 참, and에서 먼저 계산된 쪽이 거짓이면 거짓