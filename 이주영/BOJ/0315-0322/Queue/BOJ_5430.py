import sys
from collections import deque

def AC():
    global q
    # 매번 뒤집으면 시간초과 나서 짝수번 뒤집으면 똑같은 것을 활용
    isreverse = False
    for p in P:
        if p == 'R':
            # True <-> False 바꿔줌
            isreverse = not isreverse
        elif p == 'D':
            # q가 비어있지 않으면,
            if q:
                # 뒤집어야한다면 뒤에서 pop
                if isreverse:
                    q.pop()
                # 안뒤집은거랑 똑같다면 앞에서 pop
                else:
                    q.popleft()
            # q가 비어있으면 error
            else:
                return 'error'
    # 뒤집어야하면 뒤집기
    if isreverse:
        q.reverse()
    # 덱을 리스트로 만들고 그 리스트를 문자열로 만든 뒤, 빈공간을 없애줌
    return str(list(q)).replace(' ', '')


T = int(sys.stdin.readline())
for t in range(T):
    P = sys.stdin.readline()
    N = int(sys.stdin.readline())
    # 빈 배열일때는 그냥 빈 덱 만들어주기
    if N == 0:
        sys.stdin.readline()
        q = deque()
    # 양쪽 괄호 빼고 콤마를 기준으로 리스트 만들기
    else:
        q = deque(map(int, sys.stdin.readline().rstrip()[1:-1].split(',')))
    print(AC())