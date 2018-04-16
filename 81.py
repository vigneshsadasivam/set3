n=int(input("Enter the number of lines"))
b=[]
for i in range(n):
    x,y=map(int,input().split(' '))
    a=(abs(x-y))
    b.append(a)
for i in b:
  print(i)
