n = int(input())
result =[]

for i in range(1,n+1):
    clap = 0
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        clap += str(i).count('3')
        clap += str(i).count('6')
        clap += str(i).count('9')
        result.append('-'*clap)
    else:
        result.append(str(i))

print(' '.join(result))
