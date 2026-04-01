class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin = curMax = 1
        result = nums[0]
        for num in nums:
            temp = curMax * num
            curMax = max(num, num * curMax, num * curMin)
            curMin = min(num, temp, num * curMin)
            result = max(result, curMax)
        return result

