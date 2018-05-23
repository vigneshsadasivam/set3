n,k=map(int,input("Enter the number:").split(" "))
a=[]
for i in range(0,n):
  b=int(input())
  a.append(b)
s=[]
for i in a:
  if(i%2!=0):
    s.append(i)
print(s[k-1])
