# 1863. Sum of All Subset XOR Totals
# https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums):
        total_nums = []
        total_arr = []
        
        def xorOperate():            
            cur_num = 0
            for num in total_arr:
                cur_num ^= num
            total_nums.append(cur_num)

                
        def backtracking(i):
            if i == len(nums):
                return 
            total_arr.append(nums[i])
            backtracking(i+1)
            xorOperate()
            total_arr.remove(nums[i])
            backtracking(i+1)
            
        backtracking(0)
        return sum(total_nums)




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

