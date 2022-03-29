import sys

def dfs(s):
    global ans

    if len(start) == N//2:
        link = []
        for i in range(N):
            if i not in start:
                link.append(i)
        diff = cal_diff(start, link)
        ans = min(ans, diff)
        return

    for i in range(s, N):
        if i not in start:
            start.append(i)
            dfs(i+1)
            start.pop()

def cal_diff(s, l):
    s_power = l_power = 0
    for i in range(N//2):
        for j in range(N//2):
            s_power += arr[s[i]][s[j]]
            l_power += arr[l[i]][l[j]]
    return abs(s_power - l_power)


N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
start = []
ans = 1e9
dfs(0)
print(ans)