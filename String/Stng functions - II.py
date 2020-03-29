#User function Template for python3

# Function to check if string 
# starts and ends with 'gfg'
def gfg(a):
    b = a.lower()
    if((b.startswith('gfg') or b.startswith('GFG')) and b.endswith('gfg') or b.endswith('GFG')):  # use b.startswith() and b.endswith()
        print ("Yes")
    else:
        print ("No")