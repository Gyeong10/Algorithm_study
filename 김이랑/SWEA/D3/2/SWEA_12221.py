case_num = int(input())
for test_case in range(1, case_num+1):
    a, b = map(int, input().split())

    if a < 10 and b < 10:
        print(f"#{test_case} {a*b}")
    else:
        print(f"#{test_case} {-1}")