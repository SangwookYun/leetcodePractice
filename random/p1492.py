# 1143. Longest Common Subsequence
class Solution:
     def kthFactor(self, n, k):
        cur =1
        factor = []
        while cur <int(n/2):
            if n%cur == 0:
                factor.append(cur)
                factor.append(int(n/cur))
            cur+=1
        print(factor)
        factor = sorted(list(set(factor)))
        

        if n ==1:
            factor.append(n)

        print(factor)
        if len(factor)<k:
            return -1
        else:
            return factor[k-1]

        
        
               
               
        

if __name__ == "__main__":
    solution = Solution()
    
    #TestCase1
    print("TESTCASE1")
    n, k =12,3
    print("PASS" if solution.kthFactor(n, k) == 3 else "FAILED")
    print("------")

    n,k=7,2
    print("PASS" if solution.kthFactor(n, k) == 7 else "FAILED")
    print("------")
    n,k=4,4
    print("PASS" if solution.kthFactor(n, k) == -1 else "FAILED")
    print("------")
    n,k=1,1
    print("PASS" if solution.kthFactor(n, k) == 1 else "FAILED")
    print("------")