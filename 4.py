#Move all zeros to end
arr = list(map(int,input("enter: ").split()))
pos = 0
n = len(arr)
for i in range(n):
    if arr[i]!= 0:
        arr[pos]=arr[i]
        pos += 1
for i in range(pos,n):
    arr[i]=0

print(arr)
