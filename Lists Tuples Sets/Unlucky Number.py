#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends

#User function Template for python3

def realSum(mylist):
    ##Your code here
    s=0
    b= mylist.count(7)
    if(b==0):
        return sum(mylist)
    else:
        while(mylist!=None):
            b= mylist.count(7)
            if(b==0):
                return s+sum(mylist)
            else:
                a=mylist.index(7)
                s=s+sum(mylist[0:a])
                mylist = mylist[a+2:]
        
            
    return s


#{ 
#Driver Code Starts.




def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        
        mylist= [int(x) for x in input().split()]
        print(realSum(mylist))
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends