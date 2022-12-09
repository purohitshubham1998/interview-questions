def is_close_string(word1, word2):
    n = len(word1)
    m = len(word2)
    v1 = [0 for i in range(26)]
    v11 = [0 for i in range(26)]
    v2 = [0 for i in range(26)]
    v22 = [0 for i in range(26)]
    for i in word1:
        result = ord(i)-ord("a")
        v1[result] += 1
        v11[result] = 1
    for i in word2:
        result = ord(i)-ord("a")
        v2[result] += 1
        v22[result] = 1
    v1.sort()
    v11.sort()
    v2.sort()
    v22.sort()
    return v1 == v2 and v11 == v22


word1 = "cabbba"
word2 = "abbccc"
result = is_close_string(word1, word2)
print(result)