class Solution:
    def findErrorNums(self, nums):
        duplicate = 0

        for i in range(len(nums)):
            if nums.count(nums[i]) == 2:
                duplicate = nums[i]
                break

        missing = 0

        for i in range(1, len(nums) + 1):
            if i not in nums:
                missing = i

        return [duplicate, missing]
