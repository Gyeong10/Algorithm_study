x, y = map(int, input().split())
rev_x = rev_y = 0
while x > 0:
    rev_x += (x % 10) * (10 ** (len(str(x))-1))
    x //= 10

while y > 0:
    rev_y += (y % 10) * (10 ** (len(str(y))-1))
    y //= 10

total = rev_x + rev_y
print(int(str(total)[::-1]))