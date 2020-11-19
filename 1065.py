num = int(input())
count = 0
if num == 1000:
    num = 999
if num < 100:
    count = num
    print(count)
else:
    count = 99
    for i in range(100,num+1):
        try:
            i_100 = int(i/100)
            i_10 = int((i-i_100*100)/10)
            i_1 = i - (i_10*10) - (i_100*100)
            
            if i_100 - i_10 == i_10 - i_1:
                count = count + 1
    
        except:
            break
    print(count)