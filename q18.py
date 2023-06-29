bin=int(input("enter num"))
dec=0
p=1
while bin!=0:
    rev=bin%10
    bin=bin//10
    dec=dec+rev*p
    p=p*2
print(dec)    