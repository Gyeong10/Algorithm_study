# 방배정
N, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# [여자학생수, 남자학생수]로 학년별로 저장할 변수 cnt 선언 및 초기화. 1~6행 사용
cnt = [[0, 0] for _ in range(7)]
room = 0
# cnt[학년][성별]에 학생수 저장
for student in arr:
    cnt[student[1]][student[0]] += 1
# 각 학년별/성별별로 계산하는데 학생수가 k로 나눠떨어지면 몫만큼만 더하고 아니면 몫 + 1 만큼 더함
for i in range(1, 7):
    for j in range(2):
        if cnt[i][j] % k:
            room += (cnt[i][j] // k) + 1
        else:
            room += (cnt[i][j] // k)
print(room)