# each grpah has water in between line and add each in between the lines 
def rain_water(arr):
    w=0
    n=len(arr)
    for i in range(n):
        j=i
        leftmax=0
        rightmax=0
        while j>=0:
            leftmax=max(leftmax,arr[j])
            j-=1
        j=i
        while j<n:
            rightmax=max(rightmax,arr[j])
            j+=1
        w+=min(leftmax,rightmax)-arr[i]
    return w 

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(rain_water(arr))            