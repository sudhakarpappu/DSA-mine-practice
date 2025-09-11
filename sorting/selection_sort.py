def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        mid=i
        for j in range(i+1,n):
            if arr[mid]>arr[j]:
                mid=j
    arr[i],arr[mid]=arr[mid],arr[i]
arr=[1,0,9,2,8,3,7,4,5,776]
selection_sort(arr)
print(arr)