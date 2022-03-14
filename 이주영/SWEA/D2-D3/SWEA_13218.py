# 3명 이상의 학생으로 구성된 조의 수의 최댓값 구하기
T = int(input())
# arr = [int(input()) for _ in range(T)]
for t in range(T):
    num = int(input())
    print(f'#{t+1} {num//3}')