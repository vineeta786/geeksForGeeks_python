cat = 0
  hat = 0
  length = len(str)
  i=0
  while(i<=length-3):
      if(str[i:i+3]=="cat"):
          cat+=1
      elif(str[i:i+3]=="hat"):
          hat+=1
      i=i+3      
  if(cat == hat):
      return True
  else:
      return False
	  