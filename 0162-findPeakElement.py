"""A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks,
 return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a 
neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time."""

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = l + (r - l) // 2
            
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        
        return r
    
print(Solution().findPeakElement(nums = [1,2,3,1]))
print('\n')
print(Solution().findPeakElement(nums = [1,2,1,3,5,6,4]))
