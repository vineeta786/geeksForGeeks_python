#User function Template for python3

def maxlength(s):
    count = 0
    maxc = -1
    
    for i in s:
        if i=='1':
            count+=1
            
        elif i=='0':
            if maxc<count:
                maxc=count
            count=0
    if count>maxc:
        maxc=count
    return maxc



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        s=input()
        print(maxlength(s))
# } Driver Code Ends