class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = nums[0]
        prev2 = 0
        for i in range(len(nums)):
            take = nums[i]
            if i > 1:
                take += prev2
            nottake = prev
            curr = max(take,nottake)
            prev2 = prev
            prev = curr
        return prev
