stu_num = int(input())
student = list(range(1, 1+stu_num))
order = list(map(int, input().split()))

for i in range(stu_num):
    # 한칸씩 뒤로 옮겨야함:
    if order[i] != 0:
        temp = student[i]
        for j in range(order[i]):
            student[i-j] = student[i-j-1]
        student[i-order[i]] = temp

print(*student)