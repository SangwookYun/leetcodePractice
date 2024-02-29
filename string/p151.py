class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        f = 0
        w = 0
        print(s)
        s = s.split()[::-1]
        print(s)
        new_str = ""
        for st in s:
            new_str = new_str+ " "+st

        return new_str.strip()
    
if __name__ == "__main__":
    solution = Solution() 
    #TestCase1
    print("TESTCASE1")
    s = "the sky            is blue"
    print(solution.reverseWords(s))
    print("------")
    # # #TestCase2
    print("TESTCASE2")
    s = "  hello world  "
    print(solution.reverseWords(s))
    print("------")
    # # #TestCase3
    print("TESTCASE3")
    s = "a good   example"
    print(solution.reverseWords(s))
    print("------")