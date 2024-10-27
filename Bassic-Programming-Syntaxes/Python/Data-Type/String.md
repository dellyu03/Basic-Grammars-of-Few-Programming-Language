# Sting
> 파이썬 문자열 자료형

## 파이썬 문자열 생성 방식

`"`. `'`, `""`, `'''`로 문자열 양쪽을 감싼다

## 특수한 문자열 사용

### 1. 작은따옴표, 큰따옴표 포함시키기

```python
# 문자열에 포함시키지 않은  기호로 문자열을 감싸면 된다.
string_example = ' "Hello world" '

# 큰따옴포를 포함시키기 위해 작은 따옴표로 문자열을 감싼다.

#이스케이프 코드 사용 (\)
string_example = "\" hello world \" "
```

### 2. 여러 줄인 문자열을 만들기
```python
# 이스케티프 코드 \n 사용
multiline = "Life is too short\nYou need Python"

# 연속된 작은따옴표 3개 또는 큰따옴표 3개 사용

multiline = '''
Life is too short
you need python
'''

```

## 문자열 연산
> 파이썬은 문자열 덧셈과 곱셈이 존재한다.

### 1) 문자열 덧셈
```python
first = "hello"
second = "world"

result = first+second

#result : hello world
```

### 2) 문자열 곱하기
```python
a = "python"

a*2 

#pythonpython
```

## 문자열 관련 함수

- `len(string)` : 문자열의 길이를 구하는 함수 (ex. len(name))
- string[number] : 문자열 인덱싱 (ex. name[3])
    - 마이너스 기호를 이용해 뒤에서 n번째의 문자열을 인덱싱 할 수 있다.
- string[n:n] : 문자열 슬라이싱 (ex. name[0:3])
    - 끝번호 생략시 문자열 끝까지 슬라이싱
    - 마이너스 기호를 포함할 수 있다.

## 문자열 포매팅
- 숫자 대입
```python
string = "I eat %d apples" % 3
```
- 문자열 대입
```python
string = "I eat %s apples" % five
```
- 변수로 대입
```python
string = "I eat %d apples" % number
```
해당 변수 타입에 맞게 포매팅
- 2개 이상 넣기
```python
string = "I eat %d apples.  so I was sick for %s days." %(number, day)
```

`c.f` 포매팅 연산자와 %를 같이 쓸 때는 %%를 써서 %기호를 표현한다.



