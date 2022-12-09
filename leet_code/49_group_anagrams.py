from typing import List, Dict
def groupAnagrams(strs: List[str]):
    frequency: Dict  = dict()
    result: List[List[str]] = []
    for s in strs:
        temp = "".join(sorted(s))
        if temp in frequency:
            result[frequency[temp]].append(s)
        else:
            result.append([s])
            frequency[temp] = len(result)-1
    print(result)


strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)