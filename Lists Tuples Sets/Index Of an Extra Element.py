def findExtra(a,b,n):
    
    #add code here
    for v in range(0,n-1):
        if(a[v]!=b[v]):
            return v
    
    return n-1        
#{ 
#  Driver Code Starts
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        print(findExtra(a,b,n))
# } Driver Code Ends