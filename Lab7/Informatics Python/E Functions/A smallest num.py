arr=[int(i) for i in input().split()]

def mini(arr):
    arr.sort()
    return arr[0]


print(mini(arr))

