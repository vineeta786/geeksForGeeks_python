#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends

#User function Template for python3

# Function to check if pair 
# with given sum exists
def pair_sum(dict, n, arr, summ):
    
    # Your code here
    # Hint: You can use 'in' to find if any key is in dict
    
    for v in range(n):
        for k in range(v+1,n):
            if(arr[v]+arr[k]== summ):
                return True
            
        
    
    return False


#{ 
#Driver Code Starts.
# Driver code
def main():
    
    # testcase input
    testcase = int(input())
    
    # looping through testcases
    while(testcase > 0):
        
        n = int(input())
        sum = int(input())
        dict = {}
        x = n
        p = [int(i) for i in (input().split())]
        
        for i in p:
            dict[i] = 0
                
        for i in p:
            dict[i] +=1
    
        if pair_sum(dict, n, p, sum) is True:
            print ("Yes")
        else:
            print ("No")
        
        testcase -= 1


if __name__ == '__main__':
    main()
#} Driver Code Ends