def insertsort(arr):
    n=len(arr)
    if n<=1:
        return
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
ar=[1,2,8,6,4,3,56,7,6,8]
insertsort(ar)
print(ar)
