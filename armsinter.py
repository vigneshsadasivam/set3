n=int(input("Enter starting number "))
e=int(input("enter last number"))
for i in range(n,e+1):
  s=len(str(i))
  sum = 0
  temp =i
  while temp > 0:
    digit = temp % 10
    sum =sum+ digit ** s
    temp =temp//10
  if i == sum:
      print(i)

