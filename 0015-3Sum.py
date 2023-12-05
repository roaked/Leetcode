# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
#i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

class Solution(object):
    def threeSum(self, nums): # int[nums] type list       
        num_idx = {} 
        final = []
        counter = []
        while (len(counter) <= 3):
            for idx, num in enumerate(nums): # type list ---> Pos. 0 / 1
                if nums[idx]:
                    #return [num_idx[num],idx]
                    return final[nums[idx]]
                else:
                    num_idx[num]

nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))

nums = [0,1,1]
print(Solution().threeSum(nums))

nums = [0,0,0]
print(Solution().threeSum(nums))