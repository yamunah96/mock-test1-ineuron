
def moveZeroes(nums):
    left = 0  # pointer to place non-zero elements
    right = 0  # pointer to iterate through the array

    while right < len(nums):
        if nums[right] != 0:
            # swap non-zero element to the correct position
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1

    # fill the remaining elements with zeros
    while left < len(nums):
        nums[left] = 0
        left += 1

    return nums

nums1 = [0, 1, 0, 3, 12]
print(moveZeroes(nums1))
# Output: [1, 3, 12, 0, 0]

nums2 = [0]
print(moveZeroes(nums2))
# Output: [0]