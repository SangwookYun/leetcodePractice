# 78. Subsets

class Solution:
    def subsets(self, nums):
        ans = []
        cur = []
        def backtracking(i):
            if i == len(nums):
                return
            cur.append(nums[i])
            backtracking(i+1)
            print(cur)
            ans.append(cur.copy())
            cur.remove(nums[i])
            backtracking(i+1)
        backtracking(0)
        ans.append([])
        return ans



if __name__ == "__main__":
    solution = Solution()
    
    #TestCase1
    print("TESTCASE1")
    arr1 = [1,2,3]
    # print("PASS" if len(solution.subsets(arr1)) == 7 else "FAILED")
    print(solution.subsets(arr1))
    # print([[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
    print("------")
    #TestCase2
    print("TESTCASE2")
    arr2 = [5,1,6]
    # print("PASS" if len(solution.subsets(arr2)) == 1 else "FAILED")
    print(solution.subsets(arr2))
    # print([[],[0]])
    print("------")

