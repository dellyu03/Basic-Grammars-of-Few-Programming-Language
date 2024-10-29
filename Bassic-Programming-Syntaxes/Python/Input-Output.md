# input, Output
> 파이썬의 입력과 출력

## 입력

### input()
```python
a = input()
```
- 문자열 입력을 받은 후 형변환을 거친후 문자열을 반환


## 출력

`print()`를 이용한다.

### 문자열 연산
```python
print("life" "is" "too short")
print("life"+"is"+"too shor")
# 두 코드의 결과값은 같다
```

### 띄어쓰기
,로 분류된 print의 각 인자는 띄어쓰기 후 출력된다.

### 끝 문자 지정
```pytohn
print(i, end='')
```

end 매개변수를 이용해 끝문자를 지정해 줄 수 있다. 이를 통해 `이스케이프 코드`를 제거하거나 추가할 수 있다.
