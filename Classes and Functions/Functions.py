#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends

#User function Template for python3

##Write the function completely
def isPrime(n):
    flag=0
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            flag=1
            break
    
    if(flag==0):
        return True
    else:
        return False
    



#{ 
#Driver Code Starts.


import math ##You will need this for prime checking

    

def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        number=int(input())
        print(isPrime(number)) ##This isPrime is function that you need to create
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends