# String
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

## 문자열 인덱싱, 슬라이싱

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

- 정렬과 공백
```python
" %10s" % "hi" # 전체 길이를 10으로 하고 오른쪽 정렬 반대로 왼쪽 정렬은 - 빈 공간은 공백으로 놔둠

```

- 소수점 표현
```python
"0.4f" % 3.161592 # 소수점 이하 4번째 자리까지만 표현
"10.4f" % 3.161592 # 전체 길이를 10으로 두고 소수점 이하 4번째 자리까지만 표현 하고 오른쪽 정렬
```

## format 함수
```python
#인덱스
string = " one, {0}, three {1} ".format("two", "three")
 
#이름으로 넣기
string = "Hello {lang}".format(lang="python")

#정렬
{0:<10} 왼쪽 정렬
{0:>10} 오른쪽 정렬
{0:^10} 가운데 정렬
{0:=^10} 가운데 정렬 하며 공백을 =로 채움
{0:10.4f} 소수점 표현
{{ and }} 중괄호 표현

```

## f문자열 포매팅
위 기능에 추가적으로 표현식을 지원함 (ex. 10+1) 

## 문자열 관련 함수
> 자주 사용하는 함수 기준
 - `count()` : 문자열중 인자에 들어간 문자의 개수를 세준다.  (ex. string.count(b) )
 - `find` : 문자열 중 인자에 들어간 문자가 처음 들어간 인덱스를 반환한다. 없으면 -1
 - `index` : find와 같은 기능이지만 없으면 오류를 반환한다.
 - `join` : 인자로 들어간 문자열의 문자들 사이에 원하는 문자를 삽입한다. ( ex. ",".join(abcd) )
 - `upper`, `lower` : 대문자, 소문자 변환
 - `strip`, `lstrip`, `rstrip` : 양쪽 공백 제거, 가장 왼쪽 공백 제거, 가장 오른쪽 공백 제거
 - `replace` : 인자로 들어간 문자열을 특정 문자열로 바꾼다. (ex. string.replace("원래", "바꿀거"))
 - `split` : 문자열을 인자 기준으로 나눈다.


## 코딩 테스트 메모