from typing import List
# from ..trie import trie
strs = ["flower","flow","flight"]
def find_longest_commong_substring(strs: List[str]):
    trie = {}
    temp = trie
    for i in strs[0]:
        if i not in temp:
            temp[i] = {}
        temp = temp[i]
    final_string = strs[0]
    for x in strs[1:]:
        temp = trie
        temp_string = ""
        for char in x:
            if char in temp:
                temp_string += char
                temp = temp[char]
            else:
                break
        if len(final_string) > len(temp_string):
            final_string = temp_string
    return final_string


print(find_longest_commong_substring(strs))