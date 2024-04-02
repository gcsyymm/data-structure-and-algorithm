# def LCS(s1: str, s2: str) -> int:
#     if not s1 or not s2:
#         return 0
#     elif s1[-1] == s2[-1]:
#         return LCS(s1[:-1], s2[:-1]) + 1
#     else:
#         return max(LCS(s1[:-1], s2), LCS(s1, s2[:-1]))


def LCS(s1: str, s2: str) -> int:
    res = ""
    dp = [[0 for j in range(len(s1)+1)] for i in range(len(s2)+1)]
    for i in range(1, len(s2)+1):
        for j in range(1, len(s1)+1):
            if s1[j-1] == s2[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    x, y = len(s1), len(s2)
    while x != 0 and y != 0:
        if dp[y][x] == dp[y][x-1]:
            x -= 1
        elif dp[y][x] == dp[y-1][x]:
            y -= 1
        else:
            res += s1[x-1]
            x -= 1
            y -= 1
    return res


ss1 = "gxtxayb"
ss2 = "aggtab"
print(LCS(ss1, ss2))
