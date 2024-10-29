# if

## I. 기본 구조
```python
if 조건문:
    수행문1
    수행문2
    수행문3
```
- 조건문: 참인지 거짓인지 판단될 대상
- 수행문 : 조건문이 참이면 수행될 프로그래밍 문
- `c.f` 들여쓰기를 무시하면 오류가 발생한다.

## II. else, elif
조건문이 참이 아닐 경우 실행

- else: 추가 조건x
```python
if 조건문:
    수행문1
    수행문2
    수행문3
else:
    수행문
```

- elif: 추가 조건 O

## III. 파이썬 특유 조건문
> in, not in 요소가 특정 리스트/튜플에 있는지 없는지 확인

x in List/tuple

```python
a = [1, 2, 3]
1 in a # true
4 in a # false
4 not in a # true
```

## IV. 가독성 높이기
### 1. 한줄로 작성
```python
if 'money' in pocket: pass
else: print("빚을 진다")
```
### 2. 조건부 표현식
```python
message = "success" if score >= 60 else "failure"
# 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
```

