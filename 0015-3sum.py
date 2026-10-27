class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # given an integer array nums
        # return all the triples with different index, i,j,k
        # and nums[i] + nums[j] + nums[k] adds up == 0

        # Example: nums = [-1,0,1,2,-1,-4]
        # output: [[-1-1,2], [-1,0,1]]
        # output will be a list of lists of 3 sums to 0

        # for two sum II, we have sorted array, and we use two pointers, l+=1, r-=1,...
        # for this, we need to sort the nums first
        # then for each num
        # make l and r pointers, 
        # skip if nums[i] == nums[i-1]
        # check if == 0
        # l+=1
        # r-=1

        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                elif s < 0:
                    l += 1
                else: 
                    r -= 1    

        return res        
