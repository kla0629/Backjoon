def solve(a):
    ans = 0
    for i in range(len(a)):
        try:
            ans = ans + a[i]
        except:
            break
    return ans