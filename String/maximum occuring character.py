#User function Template for python3


'''
	Your task is to return the lexicographically smallest 
	max occuring charcter in given string.
	
	Function Arguments: s (given string)
	Return Type: char or -1.
	
'''

def getMaxOccurringChar(s):
    l = [0 for i in range(123)]
    
    for i in s:
        l[ord(i)]+=1
    m = max(l)
    c = l.index(m)
    return chr(c)



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        print(getMaxOccurringChar(s))
# } Driver Code Ends