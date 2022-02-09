import sys

sys.stdin = open("sample_input.txt", "r")
case_num = int(input())
for test_case in range(1, case_num + 1):
    a, b = map(int, input().split())
    time = a + b
    if time > 23:
        time = time - 24
    print(f"#{test_case} {time}")
