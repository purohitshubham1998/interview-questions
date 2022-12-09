def top_k_frequenct_number(k, array):
    n = len(array)
    count = {}
    frequency = [[] for _ in range(n+1)]
    for i in array:
        count[i] = count.get(i, 0) + 1
    for key, value in count.items():
        frequency[key].append(value)
    numbers = []
    for i in range(len(frequency)-1, 0, -1):
        for j in frequency[i]:
            numbers.append(j)
            if len(numbers) == k:
                return numbers

array = [1, 1, 1, 2, 2, 3]
res = top_k_frequenct_number(2, array)
print(res)