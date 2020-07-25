def fibdp(n):
    if n == 1:
        t=[0,1]
        return t
    elif n == 2:
        t = [0,1,1]
        return t
    else:
        t = [0 for i in range(n+1)]
        t[1]=1
        t[2]=1
        for i in range(3,n+1):
            t[i]=t[i-1]+t[i-2]
            if t[i]>n:
                return t
        return t
def evenSum(n):
    sums=0
    ans = fibdp(n)
    del ans[0]
    for i in ans:
        if i%2==0 and i<=n:
            if i==0:
                break
            else:
                sums+=i
    return sums

for _ in range(int(input())):
    
    n = int(input())
    ans = evenSum(n)
    print(ans)
    