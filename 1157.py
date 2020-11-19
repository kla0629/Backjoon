a = input().upper()
b = []
for i in range(ord('A'),ord('Z')+1):
    try:
        b.append(0)
        for j in range(len(a)):
            if ord(a[j]) == i:
                b[i-ord('A')] = b[i-ord('A')] + 1
    except:
        break

max = b[0]
index = 0
for i in range(26):
    try:
        if b[i] >  max:
            max = b[i]
            index = i
    except:
        break
count = 0
for i in range(26):
    try:
        if max == b[i]:
            count = count + 1

    except:
        break
if count >= 2:
    print("?")
else:
    print(chr((ord('A')+index)))