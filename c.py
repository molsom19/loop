n=int(input("enter no"))
i=1
count=0
while i<=n:
    if n%i==0:
        count=count+1
    else:
        pass
    i=i+1
if count==2:
    print("prime no")
else:
    print("not prime no")            