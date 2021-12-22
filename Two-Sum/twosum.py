class Solution(object):
    def twoSum(self, nums, target):
        arr = {} #array to hold integers
        #scan hash table
        for i, num in enumerate(nums):
            diff = target - num
            #meet criteria?
            if diff in arr:
                return [i, arr[diff]]
            arr[num] = i
        return []
"""
:type nums: List[int]
:type target: int
:rtype: List[int]
"""
    
        
        
