a = int(input())

a_10 = int(a/10)
a_1 = int(a - a_10*10)

i = 1
while True:
    try:
        b = a_1
        c = a_10 + a_1
        c_10 = int(c/10)
        c_1 = int(c - c_10*10)
        d = b*10 + c_1
        a_10 = int(d/10)
        a_1 = d - a_10*10
        if a == d:
            break
        else:
            i = i+1
    except:
        break
print(i)