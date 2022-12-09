"""Memoized version"""
# def climbing_staris(n):
#     dp = [-1] * (n + 1)
#     return func(n, dp)

# def func(n, dp):
#     if n == 0:
#         return 1
#     if dp[n] != -1:
#         return dp[n]
#     one_step = func(n-1, dp)
#     two_step = 0
#     if n-2 >= 0:
#         two_step = func(n-2, dp)
#     result = one_step + two_step
#     dp[n] = result
#     return result

"""Tabulized version"""
# def climbing_staris(n):
#     dp = [-1] * (n + 1)
#     dp[0] = 1
#     for i in range(1, n+1):
#         one_step = dp[i-1]
#         two_step = 0
#         if i - 2 >= 0:
#             two_step = dp[i-2]
#         dp[i] = one_step + two_step
#     print(dp)
#     return dp[n]

# """Space optimized version"""
def climbing_staris(n):
    one_step = 1
    two_step = 0
    for i in range(1, n+1):
        two_step = 0
        temp = one_step
        if i - 2 >= 0:
            two_step = temp
        one_step = one_step + two_step
    print(one_step)

n = 3
print(climbing_staris(n))