num=int(input("enter num"))
a=num
sum=0
while a>=0:
    digit=a%10
    sum+=digit**3
    a=a//10
    print(sum)
    if num==sum:
        print("num is a armstrong num")
    else: 
        print("num is not a armstrong num")         