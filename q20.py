a=int(input("enter num"))
p=a
rev=0
while a>0:
    n=p%10
    p=p//10
    rev=rev*10+n 
    print(rev)
if a==rev:
    print("palindrome num") 
else:
    print("not a palindrome num")           