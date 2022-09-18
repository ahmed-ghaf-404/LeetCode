class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        min_str = min(str1, str2)
        max_str = max(str1, str2)
        
        # build max_str
        # if you can't there is no common divisor
        for i in range(len(min_str), 0, -1):
            common_div = min_str[:i]
            num_iter = 1
            while len(common_div*num_iter)<len(min_str):
                num_iter += 1
            if (num_iter*common_div!=min_str):
                continue
            while len(common_div*num_iter)<len(max_str):
                num_iter += 1
            if (common_div*num_iter)==max_str:
                return common_div
        
        return ""