class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = dict()
        for i in range(len(nums)):
            if nums[i] in table:
                pass
            else:
                table[nums[i]] = i 
                
        for i in range(len(nums)):
            dif = target - nums[i]
            if (dif in table) and (table[dif]!=i) :
                return [i, table[dif]]
            
        return None 

if __name__=="__main__":
    assert(Solution().twoSum(nums=[1,2,3,6,8],target=5)==[1,2])