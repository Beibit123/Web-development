n = int(input())
a = list(map(int, input().split()))
cnt=0
for i in range(0, len(a)-1):
    if a[i+1] > a[i]:
        cnt = cnt + 1
print(cnt)