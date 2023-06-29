for i in range(1,8):
    for j in range(1,5):
        if j==1 or i==j or j==6-i:
            print('*',end=" ")
        else:
            print(" ",end=" ")    
    print()        