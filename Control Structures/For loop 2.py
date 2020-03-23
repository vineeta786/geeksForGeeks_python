''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
def stringJumper(str):
    for i in range(0,len(str),2):
        ## from 0 to length of str and skip 2
        print(str[i], end="") 
        ##printing character and separating characters by nothing




def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        mystr=(input())
        stringJumper(mystr)
        print()##separating testcases outputs by newlines
        testcases-=1
        


if __name__=='__main__':
    main()