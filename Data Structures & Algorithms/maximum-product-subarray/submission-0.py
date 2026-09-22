class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curr_max = 1
        curr_min = 1
        for num in nums:
            if num < 0:
                curr_max,curr_min = curr_min,curr_max
            curr_max = max(num,curr_max*num)
            curr_min = min(num,num*curr_min)
            res = max(res,curr_max)
        return res