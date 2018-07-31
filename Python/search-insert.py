class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)

        for i in range(0, len(nums)):
            if target < nums[i]:
                return i

        return len(nums)
