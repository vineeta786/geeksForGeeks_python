#User function Template for python3
def multiplicationTable(N):
    for i in range(1,11):
        print(i*N, end=" ")
        


def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        numbah=int(input())
        multiplicationTable(numbah)
        print()
        testcases-=1
        


if __name__=='__main__':
    main()