def two_sum(n, nums, t):
    def func(ind, target, lst):
        if target == 0:
            print("it was true")
            return True
        if ind == 0:
            if target - nums[ind] == 0:
                lst.append(nums[ind])
                return True
            return False
        pick = False
        if target >= nums[ind]:
            lst.append(nums[ind])
            pick = func(ind-1, target-nums[ind], lst)
            if pick:
                return True
            lst.pop()
        not_pick = func(ind-1, target, lst)
        return pick or not_pick
    lst = []
    result = func(n-1, t, lst)
    return lst


nums = [2,7,11,15]
target = 9
result = two_sum(len(nums), nums, target)
print(result)