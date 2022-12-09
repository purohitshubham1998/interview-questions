def canCross(ind, n, stones, current):
    if ind == n:
        return True
    if stones[ind - 1] + current == stones[ind]:
        return (
            canCross(ind + 1, n, stones, current + 1)
            or canCross(ind + 1, n, stones, current)
            or canCross(ind + 1, n, stones, current - 1)
        )
    return False


stones = [0, 1, 3, 5, 6, 8, 12, 17]
n = len(stones)

result = canCross(1, n, stones, 1)
print(result)
