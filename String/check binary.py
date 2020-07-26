# Return true if str is binary, else false
def isBinary(s):
    l = len(s)
    if l!= s.count('1')+s.count('0'):
        return 0
    else:
        return 1


#{ 
#  Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        str = input().strip()
        if isBinary(str):
            print (1)
        else:
            print (0)
# } Driver Code Ends