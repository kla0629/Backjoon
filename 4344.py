step = int(input())

for i in range(step):
    try:
        a = []
        total = 0
        a = list(map(int,input().split()))
        for j in range(a[0]):
            total = total + a[j+1]
        avg = total / a[0]
        count = 0
        for j in range(a[0]):
            if a[j+1] > avg:
                count = count + 1
        print("{:.3f}%".format(count/a[0]*100))

    except:
        break