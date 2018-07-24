class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        i = 0; j = 0 
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

