class Solution:
    def mergeAlternately(self, word1, word2) -> str:
        new_word = ""
        wp1, wp2 =0, 0        
        len_word1, len_word2 = len(word1), len(word2)
        while wp1<len_word1 and wp2<len_word2:
            new_word +=word1[wp1]
            new_word +=word2[wp2]
            wp1 +=1
            wp2 +=1
        
        while wp1<len_word1:
            new_word +=word1[wp1]
            wp1 +=1
        while wp2<len_word2:
            new_word +=word2[wp2]
            wp2 +=1
        return new_word
            


if __name__ == "__main__":
    solution = Solution() 
    #TestCase1
    print("TESTCASE1")
    word1 =  "abc"
    word2 = "pqrs"
    print(solution.mergeAlternately(word1, word2))
    print("------")
    