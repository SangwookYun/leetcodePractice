class Solution:
    def findMaxLength(self, nums):
        dic_seen = {}
        dic_seen[0] = -1

        ans = count = 0
        for i, num in enumerate(nums):
            count +=1 if num ==0 else -1

            if count in dic_seen:
                ans = max(ans, i-dic_seen[count])
            else:
                dic_seen[count] = i

        return ans
        
        