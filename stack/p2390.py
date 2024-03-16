class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        pt = 0
        while pt<len(s):
            if s[pt] != "*":
                stack.append(s[pt])
            else:
                if len(stack) !=0:
                    stack.pop()
            pt+=1
        print(stack)
        return "".join(stack) if len(stack) !=0: else ""
                

            


    
if __name__ == "__main__":
    solution = Solution() 
    #TestCase1
    print("TESTCASE1")
    s1 = "leet**cod*e"
    print(solution.removeStars(s1))
    print("------")
    # # #TestCase2
    print("TESTCASE2")
    s2 = "erase*****"
    print(solution.removeStars(s2))
    print("------")
    # # # #TestCase3
    # print("TESTCASE3")
    # s3 = "2[abc]3[cd]ef"
    # print(solution.decodeString(s3))
    # print("------")