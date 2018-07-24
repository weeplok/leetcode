class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if s=="":
        #     return 0
        # max_num = 1
        # for i in range(len(s)):
        #     for shift in range(1,len(s)-i+1):
        #         child_str = s[i:i+shift]
        #         if shift==len(set(child_str)) and shift>max_num:
        #             max_num = shift
        
        # return max_num 

        i = 0
        j= 0 
        char_set = set()
        ans = 1 
        while(i<len(s) and j<len(s)):
            if s[j] not in char_set:
                char_set.add(s[j])
                ans = max(ans,j-i+1)
                j+=1
            else:
                char_set.remove(s[i])
                i+=1

        return ans

if __name__=="__main__":

    print(Solution().lengthOfLongestSubstring("abcdefghijklmnopqrstuvwxyzABCDEqrstuvwxyzABCDEFGHIJKLMNOP"))

