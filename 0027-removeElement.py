"""Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k."""

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if not nums:
            return 0
        
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        
        return left
    
print(Solution().removeElement(nums = [3,2,2,3], val = 3))
print('\n')
    
print(Solution().removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))