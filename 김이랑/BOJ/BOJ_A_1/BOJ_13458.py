N = int(input())
students = list(map(int, input().split()))
B, C = map(int, input().split())

total = 0
for i in range(N):
    total += 1
    left_student = students[i] - B
    if left_student > 0:
        if left_student % C:
            total += 1
        total += left_student // C

print(total)