def remove1(n,a):
    first=n[:a]
    last=n[a+1:]
    print(first+last)
n=input("enter string:")
a=int(input("enter index number:"))
remove1(n,a)