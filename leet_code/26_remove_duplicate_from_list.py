nums = [0,0,1,1,1,2,2,3,3,4]
left = right = 1
n = len(nums)
for i in range(1, n):
    if nums[right-1] == nums[right]:
        right += 1
    else:
        nums[left] = nums[right]
        left += 1
        right += 1
print(nums)