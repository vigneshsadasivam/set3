n=int(input("enter number"))
if n==1 or n==0:
  print("neither prime nor composite")
elif n>1:
  for i in range(2,n):
    if(n%i==0):
      print("no")
      break
  else:
      print("yes")
