def maxSubarraySum(arr, k):
    n=len(arr)
    s=sum(arr[:k])
    m=s
    for i in range(k,n):
        s+=arr[i]-arr[i-k]
        m=max(m,s)
    return m
arr=[100, 200, 300, 400]
k=2

print(maxSubarraySum(arr,k))