def twosum(arr,target,skip=set()):
    res=set()
    h={}
    for i in range(len(arr)):
        if i in skip:
            continue
        y=target-arr[i]
        if y in h and h[y]!=i:
            res.add(tuple(sorted([arr[i],y])))
        h[arr[i]]=i
    return res

def fsum(arr,target):
    result=set()
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            y=target-(arr[i]+arr[j])
            t=twosum(arr,y,skip={i,j})
            for k in t:
                res1=tuple(sorted([arr[i],arr[j]])+list(k))
                result.add(res1)
    return [list(t) for t in result ]


# Example usage
nums = [2, 2, 2, 4, 2, 2, 4, 2, 0,0,0,10,2]
target = 8
print(fsum(nums, target))  # Expected: []
