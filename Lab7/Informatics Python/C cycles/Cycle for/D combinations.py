n = int(input())
k = int(input())

cnt1 = 1
cnt2 = 1
cnt3 = 1
a = n - k
for i in range (1,n+1):
    cnt1 = cnt1 * i
for i in range (1,a+1):
    cnt2 = cnt2 * i
for i in range (1,k+1):
    cnt3 = cnt3 * i

print(cnt1 /(cnt2 * cnt3))