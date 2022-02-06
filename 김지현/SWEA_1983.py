test = int(input())
grades = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

for t in range(1,test+1):
    n, k = map(int,input().split())
    #등급별 학생 수
    percentage = n//10
    total_score = []
    #점수 입력받아서 총점 구하기
    for student in range(n):
        score = list(map(int, input().split()))
        total_score.append(score[0]*0.35 + score[1]*0.45 +score[2]*0.2)

    #k의 총점    
    k_score = total_score[k-1]
    #총점 정렬
    total_score.sort(reverse=True)
    #k의 등급 index 구하기
    k_grade = total_score.index(k_score) //percentage

    print(f'#{t} {grades[k_grade]}')