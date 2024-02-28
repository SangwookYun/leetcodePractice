class Solution:
    def groupAnagrams(self, strs):
        hashmap = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in hashmap.keys():
                hashmap[sorted_word].append(word)
            else:
                hashmap[sorted_word] = [word]
            
        return hashmap.values()

if __name__ == "__main__":
    solution = Solution()
    
    #TestCase1
    print("TESTCASE1")
    strs1 = ["eat","tea","tan","ate","nat","bat"]
    # print("PASS" if solution.groupAnagrams(strs1) == 4 else "FAILED")
    print(solution.groupAnagrams(strs1))
    print("------")
    #TestCase2
    print("TESTCASE2")
    strs2 = [""]
    print(solution.groupAnagrams(strs1))
    print("------")
    #TestCase3
    print("TESTCASE3")
    strs3 = ["a"]
    print(solution.groupAnagrams(strs3))
    print("------")
