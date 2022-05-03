X = int(input())
pros = dict()
for i in range(X):
    a, arrow, b = map(str, input().split(' '))
    pros[a] = b
print(pros)