a, b = input().split()

ans = 0
l = 0

while True:
    if l == len(b):
        break
    f = False
    for i in range(len(a)):
        if a[i] == b[l]:
            f = True
            l += 1
    if not f:
        ans = -1
        break
    ans += 1

print(ans)
