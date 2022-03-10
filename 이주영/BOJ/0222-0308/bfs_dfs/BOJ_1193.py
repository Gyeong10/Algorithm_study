n = int(input())
s = 0
for visit in range(1, n+1):
    if n - visit <= 0:
        s = visit
        break
    n -= visit

if s % 2:
    s += 1
    print(f'{s-n}/{n}')
else:
    s += 1
    print(f'{n}/{s-n}')