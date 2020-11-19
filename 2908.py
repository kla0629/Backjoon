a = input().split()
b = []
for i in range(2):
    try:
        b.append(0)
        for j in range(3):
            b[i] = b[i] + int(a[i][2-j])*pow(10,2-j)
    except:
        break

if b[0] > b[1]:
    print(b[0])
else:
    print(b[1])

