nums = [1,3,5,6]
target = 7
def searchInsert(nums, target: int) -> int:
    n = len(nums)
    result = n
    for idx, value in enumerate(nums):
        if value == target or value > target:
            result = idx
            break
    return result

print(searchInsert(nums, target))