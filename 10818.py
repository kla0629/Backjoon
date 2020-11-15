step = int(input())

a = list(map(int,input().split()))

min = a[0]
max = a[0]

for i in range(step):
    if a[i] < min:
        min = a[i]
    
    if a[i] > max:
        max = a[i]

print(min, max)