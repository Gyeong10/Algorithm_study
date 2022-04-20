import sys
sys.stdin = open("sample_input.txt", "r")
case_num = int(input())
result = []
for test_case in range(1, case_num+1):
    a, b, c, d = map(int, input().split())
    # 축 하나를 고정
    time = 0
    if a <= c:
        if c < b:
            time_a = d - c
            time_b = b - c
            if time_a > time_b:
                time = time_b
            else:
                time = time_a

    else:
        if a < d:
            time_a = b - a
            time_b = d - a
            if time_a > time_b:
                time = time_b
            else:
                time = time_a
    result.append(time)

for test_case in range(1, case_num+1):
    print('#%d %d' %(test_case, result[test_case-1]))