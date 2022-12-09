def generate_parenthses(n):
    stack = []
    result = []
    def func(open, close, stack):
        if open == close == n:
           result.append("".join(stack))
           return
        if open < n:
            stack.append("(")
            func(open+1, close, stack)
            stack.pop()
        if close < open:
            stack.append(")")
            func(open, close+1, stack)
            stack.pop()
    func(0, 0, stack)
    return result

n = 3
result = generate_parenthses(n)
print(result)