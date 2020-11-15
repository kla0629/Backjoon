a = []
b = 1
for i in range(3):
    a.append(int(input()))
    b = b*a[i]

b = str(b)
c = []
d = []
for i in range(10):
    d.append(0)


for i in range(len(b)):
    c.append(int(b[i]))
    d[c[i]] = d[c[i]] + 1

for i in range(10):
    print(d[i])