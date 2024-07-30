# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count0, count1, count2 = 0, 0, 0
        
        # First pass to count the numbers of 0s, 1s, and 2s
        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            elif num == 2:
                count2 += 1
        
        # Second pass to overwrite the array with the counted numbers
        for i in range(count0):
            nums[i] = 0
        for i in range(count0, count0 + count1):
            nums[i] = 1
        for i in range(count0 + count1, count0 + count1 + count2):
            nums[i] = 2

           