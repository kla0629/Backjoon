a = []

for i in range(10):
    a.append(int(input())%42)

count = 0
check = 0

for i in range(10):
    for j in range(9-i):
        try:
            if a[i] == a[j+1+i]:
                check = 1
    
        except:
            break
    if check == 0:
        count = count + 1
    check = 0

print(count)