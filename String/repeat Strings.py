# Function to join given strings
def combo_string(a, b):
  
  # your code here
  a_len = len(a)
  b_len = len(b)
  
  if(a_len>b_len):
      short = b
      longer = a
          
  else:
      short = a
      longer = b
  return short+longer+short