array = [3, 0, 1]
res = len(array)
for i in range(len(array)):
    res += i - array[i]
print(res)