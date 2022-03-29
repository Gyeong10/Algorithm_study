from collections import deque

N = int(input())

tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)


#bfs 사용하면 1에서 가까운거 순으로 출력하니까 연결된거 알수있음
def bfs(start):
    queue = deque()
    queue.append(start)
    visited = [0]*(N+1)
    visited[start] = 1
    while queue:
        now = queue.popleft()
        for node in tree[now]:
            if visited[node] == 0:
                visited[node] = 1
                # 튜플로 같이 넣어줌, 지금꺼가부모, 다음꺼가 자식임
                answer.append((node, now))
                queue.append(node)

answer = []
bfs(1)
# 솔트로 자식 기준으로 순서 정렬 후 출력
answer.sort(key=lambda x : (x[0]))
for ans in answer:
    print(ans[1])