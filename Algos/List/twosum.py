def twosum(arr,target):
    h={}
    patr=set()
    for i in range(len(arr)):
        h[arr[i]]=i
    for i in range(len(arr)):
        y=target-arr[i]
        if y in h and h[y]!=i:
            res=tuple(sorted([arr[i],y]))
            patr.add(res)
    return patr
nums = [2, 7, 11, 15,3,6]
target = 9
print(twosum(nums,target))