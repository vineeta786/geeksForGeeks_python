#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends

#User function Template for python3

# Function to calculate average
def calc_average(nums):
    
    # Your code here
    s=sum(nums)-min(nums)-max(nums)
    n=len(nums)-2
    
    s=s//n
    
    
    return s


#{ 
#Driver Code Starts.

# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        size_arr = int(input())
        
        a = input().split()
        arr = list()
        for i in range(0, size_arr, 1):
            arr.append(int(a[i]))
        
        print (calc_average(arr))
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
#} Driver Code Ends