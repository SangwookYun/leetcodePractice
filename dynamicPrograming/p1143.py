# 1143. Longest Common Subsequence
class Solution:
     def longestCommonSubsequence(self, text1, text2):
        dp = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
        
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if text1[j-1] == text2[i-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        print(dp)
        return dp[len(text2)][len(text1)]

if __name__ == "__main__":
    solution = Solution()
    
    #TestCase1
    print("TESTCASE1")
    text1 = "abcde"
    text2 = "ace" 
    print("PASS" if solution.longestCommonSubsequence(text1, text2) == 3 else "FAILED")
    print("------")
    #TestCase2
    print("TESTCASE2")
    text1 = "abc"
    text2 = "abc"
    print("PASS" if solution.longestCommonSubsequence(text1, text2) == 3 else "FAILED")
    print("------")
    #TestCase3
    print("TESTCASE3")
    text1 = "abc"
    text2 = "def"
    print("PASS" if solution.longestCommonSubsequence(text1, text2) == 0 else "FAILED")
    print("------")
    #TestCase4
    print("TESTCASE4")
    text1 ="bl"
    text2 = "yby"
    print("PASS" if solution.longestCommonSubsequence(text1, text2) == 1 else "FAILED")
    print("------")

    #TestCase5
    print("TESTCASE5")
    text1 = "aaaaa"
    text2= "aaaaaaaaa"
    
    print("PASS" if solution.longestCommonSubsequence(text1, text2) == 5 else "FAILED")
    print(solution.longestCommonSubsequence(text1, text2))
    print("------")
    
    #TestCase6
    print("TESTCASE6")
    text1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    text2 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    print("PASS" if solution.longestCommonSubsequence(text1, text2) == 210 else "FAILED")
    print("------")

    #TestCase7
    print("TESTCASE7")
    text1= "lcnqdmvsdopkvqvejijcdyxetuzonuhuzkpelmva"
    text2 = "bklgfivmpozinybwlovcnafqfybodkhabyrglsnen"
    print("PASS" if solution.longestCommonSubsequence(text1, text2) == 9 else "FAILED")
    print("------")
