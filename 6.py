#Check if array is sorted
a =list(map(int,input("enter: ").split()))
n = len(a)
for i in range(0,n-1):
    if a[i]>a[i+1]:
        print("False")
        break
else:
    print("True")
