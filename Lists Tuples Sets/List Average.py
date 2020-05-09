#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends

#User function Template for python3


def avg(mylist):
    ##Your Code Here
    n = len(mylist)-2
    s = sum(mylist)-max(mylist)-min(mylist)
    
    avg =s//n
    
    return avg

#{ 
#Driver Code Starts.




def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        
        mylist= [int(x) for x in input().split()]
        print(avg(mylist))
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends