def maxAlternatingSum(nums):
    sumEven, sumOdd = 0, 0
    for i in range(len(nums) - 1, -1, -1):
        tempEven = max(sumOdd + nums[i], sumEven)
        tempOdd = max(sumOdd - nums[i], sumEven)
        sumEven, sumOdd = tempEven, tempOdd
    return sumEven

    dp = {}

    def dfs(i, even):
        if i == len(nums):
            return 0

        if (i, even) in dp:
            return dp[(i, even)]

        total = nums[i] if even else (-1 * nums[i])
        dp[(i, even)] = max(total + dfs(i + 1, not even), dfs(i + 1, even))
        return dp[(i, even)]

    return dfs(0, True)