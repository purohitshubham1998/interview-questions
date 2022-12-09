nums = [4,2,4]
def find_subarray_with_equal_sum(n, array):
    def func(ind, array, subarray, total):
        if ind == 0:
            return array[ind]
        pick = func(ind, array, subarray.append(array[ind]), total+array[ind])
        not_pick = 0 + 
    func(n-1, array, [], 0)

find_subarray_with_equal_sum(len(nums), nums)