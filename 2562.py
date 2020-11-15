a = []

for i in range(9):
    try:
        a.append(int(input()))
    except:
        break

max_index = 0
max = 0

for i in range(9):
    try:
        if max < a[i]:
            max_index = i
            max = a[i]
    except:
        break

print(max)
print(max_index+1)
