class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin = nums[0]
        curMax = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]

            tempMax = max(num, num * curMax, num * curMin)
            tempMin = min(num, num * curMax, num * curMin)

            curMax = tempMax
            curMin = tempMin

            result = max(result, curMax)
        return result