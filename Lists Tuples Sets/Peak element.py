# your task is to complete this function
# function should return index to the any valid peak element
def peakElement(arr, n):
    # Code here
    
    if(n>1):
        for v in range(1,n-1):
            if(arr[v]>arr[v+1] and arr[v]>arr[v-1]):
                return v
                
        if(arr[0]>arr[1]):
            return 0
        elif(arr[n-1]>arr[n-2]) :
                return n-1

    else:
        return 0

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = peakElement(arr, n)
        flag = False
        if index == 0 and n==1:
            flag = True
        elif index==0 and arr[index]>=arr[index+1]:
            flag = True
        elif index==n-1 and arr[index]>=arr[index-1]:
            flag = True
        elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
            flag = True
        else:
            flag = False

        if flag:
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends