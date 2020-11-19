step = int(input())

a = []
out = []

count = 0
total = 0
for i in range(step):
    try:
        a = str(input())
        for j in range(len(a)):
            if a[j] == 'O':
                count = count + 1
            elif a[j] == 'X':
                count = 0
            total = total + count
        print(total)
        total = 0
        count = 0
    except:
        break  