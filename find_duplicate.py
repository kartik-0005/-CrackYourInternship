# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space

class Solution(object):
    def findDuplicate(self, nums):

        nums.sort()
        for i in range(len(nums)):
            if nums[i]==nums[i+1]:
                return nums[i]
        return 0

        