#Rotate array by one
arr=list(map(int,input("enter: ").split()))
n = len(arr)
last = arr[-1]
for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
arr[0]=last

print(arr)