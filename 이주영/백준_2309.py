# 일곱 난쟁이
arr = [int(input()) for _ in range(9)]
total = 0
# 버블정렬 + 합구하기
for i in range(8, 0, -1):
    for j in range(i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
    total += arr[i]
# 첫번째 값은 total에 안 더해져서 더해주고 100을 빼 진짜 난쟁이가 아닌 사람의 키의 합계 구하기
total = total + arr[0] - 100
# 난쟁이 아닌 사람 인덱스 담을 변수 선언 및 초기화
no = []
# 두개의 값이 난쟁이가 아닌 사람의 키 합계와 같으면 그 인덱스 저장하고 break
for i in range(9):
    for j in range(i+1, 9):
        if total == arr[i] + arr[j]:
            no = [i, j]
            break
# 이건 슬라이싱인데 이렇게 하면 안 좋을 것 같아서 다른 방법으로 풀었음
# result = arr[:no[0]] + arr[no[0]+1:no[1]] + arr[no[1]+1:]
# print(*result, sep='\n')

# no리스트에 인덱스가 있으면 출력 안하고 없으면 출력
for i in range(9):
    if i in no:
        continue
    print(arr[i])