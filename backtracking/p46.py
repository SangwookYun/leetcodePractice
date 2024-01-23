# 46. Permutations

class Solution:
    def permute(self, nums):
        pass


if __name__ == "__main__":
    solution = Solution()
    
    #TestCase1
    print("TESTCASE1")
    arr1 = [1,3]
    print("PASS" if solution.subsetXORSum(arr1) == 6 else "FAILED")
    print(solution.subsetXORSum(arr1))
    print("------")
    #TestCase2
    print("TESTCASE2")
    arr2 = [5,1,6]
    print("PASS" if solution.subsetXORSum(arr2) == 28 else "FAILED")
    print(solution.subsetXORSum(arr2))
    print("------")
    #TestCase3
    print("TESTCASE3")
    arr3 = [3,4,5,6,7,8]
    print("PASS" if solution.subsetXORSum(arr3) == 480 else "FAILED")
    print(solution.subsetXORSum(arr3))
    print("------")

