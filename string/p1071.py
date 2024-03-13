class Solution:
    def gcdOfStrings(self, word1, word2) -> str:
        
        
        short = word1 if len(word1) <= len(word2) else word2 
        long = word1 if len(word1) > len(word2) else word2 
        short_len = len(short)
        long_len = len(long)
        gcd = ""
        for i in range(len(short)+1):
            cur = short[0:i]
            cur_len = len(cur)

            if cur == "":
                continue
            if short_len % cur_len !=0:
                continue
            if long_len % cur_len !=0:
                continue
            if cur * (short_len//cur_len) == short and cur * (long_len//cur_len) == long:
                gcd = cur

        return gcd                 
            

if __name__ == "__main__":
    solution = Solution() 
    #TestCase1
    print("TESTCASE1")
    word1 =  "ABCABC"
    word2 = "ABC"
    print(solution.gcdOfStrings(word1, word2))
    print("------")
    