def heap(arr,n,i):
    large=i
    left=2*i+1
    right=2*i+2
    if left<n and arr[large]<arr[left]:
        large=left
    elif right<n and arr[large]<arr[right]:
        large=right
    if large!=i:
        arr[i],arr[large]=arr[large],arr[i]
        heap(arr,n,large)
def heap_sort(arr):
    n=len(arr)
    for i in range(n//2 -1,-1,-1):
        heap(arr,n,i)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heap(arr,i,0)

data = [4, 10, 3, 5, 1]
print("Original:", data)
heap_sort(data)
print("Sorted:", data)
