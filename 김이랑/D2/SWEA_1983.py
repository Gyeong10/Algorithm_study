# 어렵진 않은데 화나는 문제
import sys
sys.stdin = open("test_1983_input.txt", "r")

test_num = int(input())
for test_case in range(1, test_num + 1):
    students_num , student = map(int, input().split())
    student_scores = []
    # 점수낸다
    for i in range(students_num):
        mid, final, report = map(int, input().split())
        score = (mid*0.35) + (final*0.45) + (report*0.2)
        student_scores.append(score)

    # 1등이라고 가정하고 더 높은놈 있으면 등수 하나씩 떨어짐
    rank = 1
    for score in student_scores:
        if score > student_scores[student-1]:
            rank = rank + 1

    # 퍼센트별로 등급 부여.. 복붙 힘드러!
    if rank / students_num <= 0.1:
        grade = 'A+'
    elif rank / students_num <= 0.2:
        grade = 'A0'
    elif rank / students_num <= 0.3:
        grade = 'A-'
    elif rank / students_num <= 0.4:
        grade = 'B+'
    elif rank / students_num <= 0.5:
        grade = 'B0'
    elif rank / students_num <= 0.6:
        grade = 'B-'
    elif rank / students_num <= 0.7:
        grade = 'C+'
    elif rank / students_num <= 0.8:
        grade = 'C0'
    elif rank / students_num <= 0.9:
        grade = 'C-'
    elif rank / students_num <= 1:
        grade = 'D0'

    print(f'#{test_case} {grade}')
