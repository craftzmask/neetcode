class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in indices:
                return [indices[compliment], i]
            indices[num] = i
        return []