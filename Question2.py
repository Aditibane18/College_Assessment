#Question 2
def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]


def min_deletions_and_insertions(str1, str2):
    lcs_length = longest_common_subsequence(str1, str2)

    deletions = len(str1) - lcs_length
    insertions = len(str2) - lcs_length

    return deletions, insertions

str1 = "heap"
str2 = "pea"
deletions, insertions = min_deletions_and_insertions(str1, str2)

print(f"Minimum Deletion = {deletions}")
print(f"Minimum Insertion = {insertions}")
