def is_power(n):
    n = n/2
    if n == 2:
        print("s")
    elif n > 2:
        return is_power(n)
    else:
        print("no") 
s=int(input("enter a number"))
is_power(s)
