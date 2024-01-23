# 1239. Maximum Length of a Concatenated String with Unique Characters
# Medium
# You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.
# Return the maximum possible length of s.
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

class Solution:
    def maxLength(self, arr):   
        charSet = set()
        
        def overlap(charSet, s):
            prev = set()
            for c in s:
                if c in charSet or c in prev:
                    return True
                prev.add(c)
            return False
                
        def backtracking(i):
            if i == len(arr):
                return len(charSet)
            
            res = 0
            if not overlap(charSet, arr[i]):
                for c in arr[i]:
                    charSet.add(c)
                res = backtracking(i+1)
                
                for c in arr[i]:
                    charSet.remove(c)
            return max(res, backtracking(i+1))
        
        
        return backtracking(0)

if __name__ == "__main__":
    solution = Solution()
    
    #TestCase1
    print("TESTCASE1")
    arr1 = ["un", "iq", "ue"]
    print("PASS" if solution.maxLength(arr1) == 4 else "FAILED")
    print("------")
    #TestCase2
    print("TESTCASE2")
    arr2 = ["cha","r","act","ers"]
    print("PASS" if solution.maxLength(arr2) == 6 else "FAILED")
    print("------")
    #TestCase3
    print("TESTCASE3")
    arr3 = ["abcdefghijklmnopqrstuvwxyz"]
    print("PASS" if solution.maxLength(arr3) == 26 else "FAILED")
    print("------")
