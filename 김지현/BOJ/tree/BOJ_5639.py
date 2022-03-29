import sys
sys.setrecursionlimit(10**6)

def postorder(l, r):
    if l > r:
        return
    else:
        m = r + 1
        for i in range(l+1, r+1):
            if lst[l] < lst[i]:
                m = i
                break
        postorder(l+1, m-1)
        postorder(m, r)
        print(lst[l])

lst = []
while True:
    try:
        n = int(sys.stdin.readline())
        lst.append(n)
    except:
        break
N = len(lst)
postorder(0, N -1)