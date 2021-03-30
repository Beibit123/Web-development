arr=[int(i) for i in input().split()]

def xor(arr):
    if(arr[0] == 1 and arr[1] == 0 or arr[0] == 0 and arr[1] == 1):
        print(1)
    else:
        print(0)

xor(arr)