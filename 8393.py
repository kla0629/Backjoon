a = int(input())
b = 0
for i in range(a):
    try:
        b = i + 1 + b
    except:
        break

print(b)