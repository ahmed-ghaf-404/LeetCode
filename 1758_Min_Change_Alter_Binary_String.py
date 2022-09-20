# https://leetcode.com/submissions/detail/804109895/
class Solution:
    def minOperations(self, s: str) -> int:
        # [i for _ in range(len(s)) if i%2 else j]
        alt_str = [''.join([str(i) if z%2==0 else str(j) for z in range(len(s))]) for i in range(2) for j in range(2) if i!=j]
        all_ops = []
        for string in alt_str:
            ops = 0 
            for index in range(len(s)):
                if s[index] != string[index]:
                    ops += 1
            all_ops.append(ops)
                    
        return min(all_ops)
        