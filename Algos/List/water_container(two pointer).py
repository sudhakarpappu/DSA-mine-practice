#each graph as lines
def water_container(arr):
        i,j,ans=0,len(arr)-1,0
        while i<j:
                if arr[i]<=arr[j]:
                        res=arr[i]*(j-i)
                        i+=1
                else:
                        res=arr[j]*(j-i)
                        j-=1
                if ans<res:ans=res
        return ans 
height = [4,3,2,1,4]
print(water_container(height))