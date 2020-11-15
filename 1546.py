step = int(input())
a = list(map(int,input().split()))
a.sort()
max = a[step-1]

total = 0
for i in range(step):
    total = total + a[i]/max*100

total = total/step
print(total)