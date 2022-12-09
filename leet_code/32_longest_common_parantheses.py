def longest_valid_parentheses(s):
    stack = []
    lookup = {")": "("}
    count = 0
    for par in s:
        if par in lookup:
            if len(stack) > 0:
                temp = stack.pop()
                if lookup[par] == temp:
                    count += 1
        else:
            stack.append(par)
    return count * 2
# s = ""
s = "()(()" # Expected output 2
# s = ")()())"

res = longest_valid_parentheses(s)
print(res)