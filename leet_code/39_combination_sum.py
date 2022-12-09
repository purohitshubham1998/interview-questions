def combination_sum(array, target):
    n = len(array)
    lst = []
    tmp = []
    func(n-1, array, target, lst, tmp)
    print(lst)
    return lst

def func(ind, array, target, lst, tmp):
    if target == 0:
        return lst.append(tmp.copy())
    if ind == 0:
        if target % array[ind] == 0:
            res = target // array[ind]
            for i in range(res):
                tmp.append(array[ind])
            return lst.append(tmp.copy())
        return
    if target >= array[ind]:
        tmp.append(array[ind])
        func(ind, array, target-array[ind], lst, tmp)
        tmp.pop()
    func(ind-1, array, target, lst, tmp)

 
candidates = [2,3,5]
target = 8
combination_sum(candidates, target)