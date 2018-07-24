class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0
        max_num = 1
        for i in range(len(s)):
            for shift in range(1,len(s)-i+1):
                child_str = s[i:i+shift]
                if shift==len(set(child_str)) and shift>max_num:
                    max_num = shift
        
        return max_num 

if __name__=="__main__":
    
    print(Solution().lengthOfLongestSubstring("abcdefghijklmnopqrstuvwxyzABCDEqrstuvwxyzABCDEFGHIJKLMNOP"))

