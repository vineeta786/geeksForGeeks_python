def check_status(a, b, status):
##Your code here
##Either True or False is returned
if(a<0 and b<0 and status==True):
return True
elif(status==False and a*b<0):
return True
else:
return False