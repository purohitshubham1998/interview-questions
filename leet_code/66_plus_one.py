from typing import List
def plusOne(digits: List[int]) -> List[int]:
    result = 0
    multiplier = 1
    for i in reversed(digits):
        result = result + (i * multiplier)
        multiplier *= 10
    result += 1
    print(result)
    lst = []
    while result != 0:
        remainder = result % 10
        lst.append(remainder)
        result //= 10
    return lst[::-1]

print(plusOne(digits = [1,2,3]))