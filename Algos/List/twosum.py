def twosum(arr,target):
    h={}
    for i in range(len(arr)):
        h[arr[i]]=i
    for i in range(len(arr)):
        y=target-arr[i]
        if y in h and h[y]!=i:
            return [i,h[y]]
    return -1
nums = [2, 7, 11, 15]
target = 9
print(twosum(nums,target))