class Solution:
    def insertion_sort(self, lst):
        
        for i in range(1, len(lst)):
            for j in range(i-1, 0):
                if lst[j] >lst[i]:
                    lst[j], lst[i] = lst[i], lst[j]
                else:
                    break            
        return lst


if __name__ == "__main__":
    solution = Solution()
    
    #TestCase1
    print("TESTCASE1")
    nums = [1,3,4,8,7,9,3,5,1]
    print(solution.insertion_sort(nums))
    print("------")
   