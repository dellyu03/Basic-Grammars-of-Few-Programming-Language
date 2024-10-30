a, b, c = map(int, input().split())
prize = 0

if a==b==c:
    prize = 10000+a*1000
elif a in [b,c]:
    prize = 1000 + a * 100
elif b == c:
    prize = 1000 + b * 100
else:
    numbers = [a, b, c]
    numbers.sort(reverse = True)
    prize = numbers[0] * 100
print(prize)