a=int(input("enter t1 hour"))
b=int(input("enter t1 minute"))
c=int(input("enter t2 hour"))
d=int(input("enter t2 minute"))
e=a*60+b
f=c*60+d
g=e-f
print(g//60 'hr',g%60'min')
