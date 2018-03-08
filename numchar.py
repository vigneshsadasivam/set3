n=input("enter str")
c=0
d=0
for i in n:
  if(i.isdigit()):
    c=c+1
  elif(i.isalpha()):
    d=d+1
  else:
    continue
if(d>=1 and c>=1):
  print("yes")
else:
  print("no")
