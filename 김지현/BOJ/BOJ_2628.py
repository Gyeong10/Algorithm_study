w, h = map(int, input().split())
x = [0,w]
y = [0,h]
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if a == 1 :
        x.append(b)
    else:
        y.append(b)

x.sort()
y.sort()

maxW = maxH = 0
for i in range(1,len(x)):
    if x[i] - x[i-1] > maxW:
        maxW = x[i]-x[i-1]
for i in range(1,len(y)):
    if y[i] - y[i-1] > maxH:
        maxH = y[i]-y[i-1]
print(maxW*maxH)