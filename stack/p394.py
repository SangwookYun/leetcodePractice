class Solution:
    def decodeString(self, s: str) -> str:
        if len(s)==0:
            return ""
        stack = [s[0]]
        idx = 1
        ans = ""
        while stack or idx<len(s):

            while idx <len(s) and s[idx] != "]":
                stack.append(s[idx])
                idx+=1
            cur = ""
            while idx <len(s) and stack[len(stack)-1] != "[":
                cur+= stack.pop()
            stack.pop()
            cnt = ""
            while stack and stack[len(stack)-1].isnumeric():
                cnt += stack.pop()

            if '[' in stack:
                ans += int(cnt[::-1]) * (cur[::-1] + ans)
            else:
                ans += int(cnt[::-1]) * cur[::-1]
            idx +=1
        return ans
                
                

            


    
if __name__ == "__main__":
    solution = Solution() 
    #TestCase1
    print("TESTCASE1")
    s1 = "3[a]2[bc]"
    print(solution.decodeString(s1))
    print("------")
    # # #TestCase2
    print("TESTCASE2")
    s2 = "3[a2[c]]"
    print(solution.decodeString(s2))
    print("------")
    # # # #TestCase3
    # print("TESTCASE3")
    # s3 = "2[abc]3[cd]ef"
    # print(solution.decodeString(s3))
    # print("------")