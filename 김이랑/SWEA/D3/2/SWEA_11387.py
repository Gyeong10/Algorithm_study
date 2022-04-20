import sys
sys.stdin = open("sample_input.txt", "r")

case_num = int(input())
result = []
for test_case in range(1, case_num+1):
    D, L, N = map(int, input().split())
    sum_damage = 0
    for n in range(N):
        damage = D + int(D*0.01)*L*n
        sum_damage = sum_damage + damage

    result.append(sum_damage)

for test_case in range(case_num):
    print(f"#{test_case + 1} {result[test_case]}")
