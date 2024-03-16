class Solution:
    def compress(self,chars) -> str:
        
        left = 0
        right = 0
        pt = 0
        cnt = 0
        cur_ch = chars[pt]
        while right <len(chars):
            if chars[left] == chars[right]:
                cnt +=1
                right +=1
            else:
                chars[pt] = cur_ch
                pt +=1
                
                if cnt>1:

                    for ch in str(cnt):
                        chars[pt]= ch
                        pt+=1
                left = right
                cur_ch = chars[left]
                cnt = 0
                
                
        if cnt>1:
            chars[pt] = cur_ch
            pt+=1
            for ch in str(cnt):
                chars[pt]= ch
                pt+=1
        elif cnt ==1:
            chars[pt] = cur_ch
            pt+=1

        return chars[0:pt]
    
    def compress_2(self,chars) -> str:
        left = 0
        idx = 0
        while left <len(chars):
            right = left
            while right <len(chars) and chars[left] == chars[right]:
                right +=1

            chars[idx] = chars[left]
            idx +=1
            occurence = right-left
            if occurence> 1:
                for i in str(occurence):
                    chars[idx]= i
                    idx+=1 

            left = right
        
        return chars[0:idx]


        


        



        

if __name__ == "__main__":
    solution = Solution() 
    #TestCase1
    print("TESTCASE1")
    chars1 = ["a","a","a", "b","b","c","c","c"]
    chars2 = ["a"]
    chars3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    chars4 = ["a","a","a","b","b","a","a","a"]
    chars5 = ["a","a","b","b","c","c","c"]
    chars6 = ["a","a","a","a","a","b"]
    print("TESTCASE1", solution.compress(chars1) == ["a", "3", "b", "2", "c", "3"])
    print(solution.compress(chars1))
    print("TESTCASE2", solution.compress(chars2) == ["a"])
    print(solution.compress(chars2))
    print("TESTCASE3", solution.compress(chars3) == ["a", "b", "1", "2"])
    print(solution.compress(chars3))
    print("TESTCASE4", solution.compress(chars4) == ["a", "3", "b", "2", "a", "3"])
    print(solution.compress(chars4))
    print("TESTCASE5", solution.compress(chars5) == ["a", "2", "b", "2", "c", "3"])
    print(solution.compress(chars5))
    print("TESTCASE6", solution.compress(chars6) == ["a", "5", "b"])
    print(solution.compress(chars6))
    print("------")
    