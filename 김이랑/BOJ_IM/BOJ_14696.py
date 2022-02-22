test_num = int(input())
for test_case in range(test_num):
    A_card = [0] * 5
    B_card = [0] * 5
    A = list(map(int, input().split()))
    for i in range(1, A[0]+1):
        A_card[A[i]] += 1
    B = list(map(int, input().split()))
    for i in range(1, B[0]+1):
        B_card[B[i]] += 1

    winner = 'D'
    for i in range(4, 0, -1):
        if A_card[i] != B_card[i]:
            if B_card[i] > A_card[i]:
                winner = 'B'
                break
            elif B_card[i] < A_card[i]:
                winner = 'A'
                break
    print(winner)