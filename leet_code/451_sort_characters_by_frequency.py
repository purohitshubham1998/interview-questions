def frequencySort(s):
    count = [[] for _ in range(len(s)+1)]
    frequency = dict()
    for i in s:
        frequency[i] = 1 + frequency.get(i, 0)
    for key in frequency:
        val = frequency[key]
        count[val].append(key)
    final_string = ""
    for i in range(len(s), 0, -1):
        for char in count[i]:
            final_string += (char * i)
    return final_string

print(frequencySort("tree"))