def fourSum(nums, target):
    # Step 1: Sort the input array
    nums.sort()
    n = len(nums)
    quadruplets = []
    
    # Step 2: Iterate through the array to fix the first two elements
    for i in range(n - 3):
        # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            # Skip duplicate values for the second element
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            
            # Step 3: Two pointers for the remaining two elements
            left, right = j + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if current_sum == target:
                    # Step 4: Found a quadruplet
                    quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                    # Skip duplicates for the third element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for the fourth element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1  # We need a larger sum
                else:
                    right -= 1  # We need a smaller sum
    
    return quadruplets

nums = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(nums, target))
nums = [2,2,2,2,2]
target = 8
print(fourSum(nums,target))