
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
# Function to print True and False for required input
def friends_in_trouble(a_angry, b_angry):
##Your code here
    if a_angry == b_angry:
        return True
    else:
        return False

# Driver code    
def main():
    testcase = int(input())
    
    # loop for testcases
    while(testcase > 0):
        string = input().split()
        string1 = string[0]
        string2 = string[1]
        if(string1 == 'True'):
            string1 = True
        else:
            string1 = False
        
        if(string2 == 'True'):
            string2 = True
        else:
            string2 = False
            
        print(friends_in_trouble(string1, string2))
        
        testcase -= 1
    
if __name__ == '__main__':
    main()