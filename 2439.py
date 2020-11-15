step = int(input())

for i in range(step):
    for j in range(step-i-1):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    print("")