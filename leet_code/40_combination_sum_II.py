def combination_sum(array, target):
    result = []
    n = len(array)
    def func(ind, arr, tar, lst):
        if tar == 0:
            result.append(lst.copy())
            return
        for i in range(ind, n):
            if i > ind and arr[i] == arr[ind]:
                continue
            if arr[i] > tar:
                break
            lst.append(arr[i])
            func(i+1, arr, tar-arr[i], lst)
            lst.pop()
    func(0, array, target, [])
    print(result)

candidates = [10,1,2,7,6,1,5]
candidates.sort()
target = 8
print(candidates)
combination_sum(candidates, target)