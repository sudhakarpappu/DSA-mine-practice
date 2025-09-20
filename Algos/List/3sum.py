def threeSum(arr):
    n = len(arr)
    result = set()  # use set to avoid duplicate triplets

    for i in range(n):
        h = {}
        target = -arr[i]
        for j in range(i + 1, n):
            y = target - arr[j]
            if y in h:
                triplet = tuple(sorted([arr[i], arr[j], y]))
                print(triplet)
                result.add(triplet)
            h[arr[j]] = j

    return [list(t) for t in result]


# Example usage
nums1 = [-1, 0, 1, 2, -1, -4]
print("Input:", nums1)
print("Output:", threeSum(nums1))  # Expected: [[-1, -1, 2], [-1, 0, 1]]

nums2 = [0, 1, 1]
print("Input:", nums2)
print("Output:", threeSum(nums2))  # Expected: []

nums3 = [0, 0, 0]
print("Input:", nums3)
print("Output:", threeSum(nums3))  # Expected: [[0, 0, 0]]
