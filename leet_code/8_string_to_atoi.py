def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    lookup = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "0": 0,
        "-": -1,
        "+": 1
    }
    num = 0
    multiplier = 1
    position = 1
    for i in s:
        if i in lookup:
            if i == "-" or i == "+":
                multiplier *= lookup[i]
            else:
                num = (num * position) + lookup[i]
                position = 10
        else:
            break
    divider = int(1e31)
    final_number = num * multiplier
    divider = -1 * (divider -1)  if final_number > 0 else divider


s = "-91283472332"
result  = myAtoi(s)
print(result)
