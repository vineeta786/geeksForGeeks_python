#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends

#User function Template for python3


def has44(mylist):
    ##Your code here
    if(len(mylist)==1):
        return False
    else:    
        while(mylist!= None):
            b = mylist.count(4)
            if(b==0 or b==1):
                return False
            else:
                a = mylist.index(4)
                if mylist[a+1]==4 :
                    return True
                mylist=mylist[a+2:]   
    
    return False 
    


#{ 
#Driver Code Starts.




def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        
        mylist= [int(x) for x in input().split()]
        print(has44(mylist))
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends