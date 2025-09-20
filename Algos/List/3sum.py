def threeSumTarget(arr, target):
    n = len(arr)
    result = set()  # use set to avoid duplicate triplets

    for i in range(n):
        h = {}
        curr_target = target - arr[i]   # instead of fixing -arr[i], adjust to target
        for j in range(i + 1, n):
            y = curr_target - arr[j]
            if y in h:
                triplet = tuple(sorted([arr[i], arr[j], y]))
                result.add(triplet)
            h[arr[j]] = j

    return [list(t) for t in result]


# Example usage
nums1 = [-1, 0, 1, 2, -1, -4]
print("Input:", nums1)
print("Target = 0")
print("Output:", threeSumTarget(nums1, 0))   # [[-1, -1, 2], [-1, 0, 1]]

print("Target = 2")
print("Output:", threeSumTarget(nums1, 2))   # [[-1, 1, 2], [0, 2, 0] etc.])

nums2 = [0, 1, 1]
print("Input:", nums2)
print("Target = 0")
print("Output:", threeSumTarget(nums2, 0))   # []

nums3 = [0, 0, 0]
print("Input:", nums3)
print("Target = 0")
print("Output:", threeSumTarget(nums3, 0))   # [[0, 0, 0]]
