# bit-operator

[14681번 문제](https://www.acmicpc.net/problem/14681)
```python
X = int(input()) < 0
Y = int(input()) < 0
print("1243"[X + (Y << 1)])
```
비트 연산자 `<<1`을 활용하면 2배가 된다는 방식을 이용한 트릭
