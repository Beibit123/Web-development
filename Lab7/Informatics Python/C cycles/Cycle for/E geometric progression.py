a = int(input())
n = int(input())

cnt = 1

for i in range(1, n+1):
    cnt = cnt + a ** i
print(cnt)