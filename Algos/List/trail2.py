def tsum(arr):
    n=len(arr)
    res=set()
    for i in range(n):
        h={}
        target=-arr[i]
        for j in range(i+1,n):
            y=target-arr[j]
            if y in h:
                trip=tuple(sorted([arr[i],arr[j],y]))
                res.add(trip)
            h[arr[j]]=j
        return [list(t) for t in res]
nums1 = [-1, 0, 1, 2, -1, -4]
print("Input:", nums1)
print("Output:", tsum(nums1))