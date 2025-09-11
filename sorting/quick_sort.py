def quick_sort(arr):
    if len(arr)<=1:
        return arr 
    left=[]
    a=arr[-1]
    right=[]
    equal=[]
    for n in arr:
        if n>a:
            right.append(n)
        elif n<a:
            left.append(n)
        else:
            equal.append(n)
    return quick_sort(left)+equal+quick_sort(right)
# Example usage
data = [5, 3, 8, 4, -22]
print("Original:", data)
print("Sorted:", quick_sort(data))
