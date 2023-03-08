class Solution:
    def binary_search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                return self.binary_search(matrix[mid], target) != -1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                top = mid + 1

        return False