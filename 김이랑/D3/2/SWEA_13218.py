test_num = int(input())
# 뭐야 걍 나누기 3 몫인데
for test_case in range(1, test_num + 1):
    students = int(input())
    group = students // 3
    print(f"#{test_case} {group}")
