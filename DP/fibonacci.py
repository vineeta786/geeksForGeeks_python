def fibdp(n):
    if n == 1:
        t=[0,1]
        return t
    elif n == 2:
        t = [0,1,1]
        return t
    else:
        t = [-1 for i in range(n+1)]
        t[1]=1
        t[2]=1
        for i in range(3,n+1):
            t[i]=t[i-1]+t[i-2]
        return t
    

for _ in range(int(input())):
    
    n = int(input())
    t = fibdp(n)
    for i in range(1,len(t)):
        print(t[i],end=" ")
    print()