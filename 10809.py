a = input()
start = ord('a')

print_num = []

for i in range(start, start+27):
    try:
        print_num.append(-1)
        for j in range(len(a)):
            if ord(a[j]) == i:
                print_num[i-start] = j
                break
    except:
        break

for i in range(26):
    print(print_num[i],end=" ")