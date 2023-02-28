class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        for i, num in enumerate(nums):
            # skip all positive numbers since no way it can be summed to 0
            if num > 0:
                break

            # Skip any duplicated values
            if i > 0 and num == nums[i-1]:
                continue
            
            # Two sum with sorted array
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = num + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    result.append([num, nums[l], nums[r]])
                    l += 1

                    # Skip any duplicated values each time we found one triple
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                
        return result
