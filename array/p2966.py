# 46. Permutations

class Solution:
    def divideArray(self, nums, k):
        nums.sort()
        if len(nums)%3 !=0:
            return []
        cnt = 0
        temp =[]
        ans = []
        i = 0
        while i<len(nums):
            temp.append(nums[i])
            

            if cnt == 2:
                if temp[-1] - temp[0] > k:
                    return []
                ans.append(temp)
                temp = []
                cnt = 0
            else:
                cnt+=1
            i+=1
        return ans


if __name__ == "__main__":
    solution = Solution()
    
    #TestCase1
    print("TESTCASE1")
    nums = [1,3,4,8,7,9,3,5,1]
    k = 2
    print(solution.divideArray(nums, k))
    print("------")
    #TestCase2
    print("TESTCASE2")
    nums = [1,3,3,2,7,3]
    k = 3
    print(solution.divideArray(nums, k))
    print("------")
    # #TestCase3
    # print("TESTCASE3")
    # arr3 = [3,4,5,6,7,8]
    # print(solution.divideArray(nums, k))
    # print("------")

