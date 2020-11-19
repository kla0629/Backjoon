
for i in range(10000):
    try:
        count = 0
        start = i-int(len(str(i)))*10
        if start < 0:
            start = 0
        for j in range(start,i):
            a = str(j+1)
            
            self_number = j+1
            for k in range(len(a)):
                self_number = self_number + int(a[k])

            if self_number == i+1:
                count = count + 1
                break
        if count == 0:
            print(i+1)

    except:
        break
