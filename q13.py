from re import A


num=int(input("enter number"))
reverse=0
while 0<num:
    a=num%10
    reverse=(reverse*10)+a 
    num=num//10
    print(reverse)