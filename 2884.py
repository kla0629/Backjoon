hour, min = map(int, input().split())

a = hour*60 + min - 45
if a < 0:
    a = a + 24*60
ar_hour = int(a/60)
ar_min = int(a%60)

print(ar_hour, ar_min)