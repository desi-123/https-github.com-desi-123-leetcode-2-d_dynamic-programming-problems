def stoneGame(piles):
    dp = {}

    def dfs(left, right):
        if left > right:
            return 0
        if (left, right) in dp:
            return dp[(left, right)]
        even = True if (right - left) % 2 else False
        left = piles[left] if even else 0
        right = piles[right] if even else 0

        dp[(left, right)] = max(dfs(left + 1, right) + left,
                                dfs(left, right - 1) + right)

        return dp[(left, right)]

    return dfs(0, len(piles) - 1)