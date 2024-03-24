
class Solution:
    def readBinaryWatch(self, turnedOn):           
        stack = []
        candidate = [24, 12, 6, 3, 32, 16, 8, 4, 2, 1]
        res = []
        def backtracking(n):
            if n == turnedOn:
                print(stack)
                time = ""
                hour = 0
                minute = 0
                for num in stack:
                    if num%3 ==0:
                        hour+=(num//3)
                    else:
                        minute +=num

                
                if minute<10:
                    time = str(hour) + ":0" + str(minute)
                else:
                    time = str(hour) + ":" + str(minute)

                res.append(time)
                return
            
            if n<turnedOn:
                
                for num in candidate:
                    if num not in stack:
                        stack.append(num)
                        backtracking(n+1)
                        stack.pop()
        backtracking(0)
        
        return res
        


if __name__ == "__main__":
    solution = Solution()
    
    #TestCase1
    print("TESTCASE1")

    print(solution.readBinaryWatch(1))
    print("------")
    #TestCase2
    print("TESTCASE2")
    print(solution.readBinaryWatch(2))
    print("------")

