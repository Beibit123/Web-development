n = int(input())
a=[int(i) for i in input().split()]
cnt=0
isFind = False
for i in range(0, len(a)-1):
    if a[i+1] > 0 and a[i] > 0:
        print("YES")
        isFind = True
        break
    elif a[i+1] < 0 and a[i] < 0:
        print("YES")
        isFind = True
        break
if (isFind == False):
    print("NO")
