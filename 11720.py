step = int(input())
num = str(input())
return_num = 0
for i in range(len(num)):
    try:
        return_num = int(num[i]) + return_num
    except:
        break
print(return_num)