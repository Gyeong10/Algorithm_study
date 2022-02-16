N, K = map(int, input().split())

students = [list(map(int, input().split())) for _ in range(N)]
cnt = [0]*12

for i in range(N):
    for j in range(6):
        #학년별로 구분
        if students[i][1] == j+1:
            #여학생일 때
            if students[i][0] == 0:
                cnt[2*j] += 1
            #남학생일 때    
            else:
                cnt[2*j + 1] += 1
#방 갯수
room = 0
for i in range(12):
    if cnt[i] % K != 0:
        room += cnt[i] // K + 1
    else:
        room += cnt[i] // K
print(room)
