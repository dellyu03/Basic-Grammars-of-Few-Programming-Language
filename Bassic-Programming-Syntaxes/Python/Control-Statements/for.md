# for

## 기본 구조
```python
for 변수 in list/tuple/string:
    수행문1
    수행문2
```

## continue
for 문 또한 continue를 사용해서 처음으로 돌아갈 수 있다.

## range 함수
`range(10)`
0부터 10 미만의 숫자

```python
range(start, end)
```
끝 숫자는 포함하지 않는다

## 리스트 내포
```python
[표현식 for 항목 in 반복 가능 객체 if 조건]

a = [1, 2, 3, 4]
result = [num * 3 for num in a]
```