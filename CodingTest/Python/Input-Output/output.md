# Output (for Python Coding Test)
> 파이썬 코딩 테스트 관련 출력 기법 정리

# I. output 사용
> 가장 기본적인 사용 방법

[기본 입출력](../../../Bassic-Programming-Syntaxes/Python/Input-Output.md) 사용 방법

## print 추가 사용법

- ### sep vs end
    - end의 경우 모든 출력이 끝난 후 적용되며 주로 개행문자(\n)을 제거하여 여러번의 출력을 한줄에 나타내는 등의 용도로 사용된다.
    - sep(seperator)의 경우 인자간 사이사이에 적용된다. 주로 인자간 공백을 제거하거나 하나의 출력에서 줄을 나눌때도 사용될 수 있다.



```python
print("hello", "world", sep(/)

# --> hello/world
```