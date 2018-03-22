n=int(input("enter n"))
i=0
f=0
s=1
while(i<n):
  if(i<=1):
    x=i
  else:
    x=f+s
    f=s
    s=x
  print(x)
  i=i+1
