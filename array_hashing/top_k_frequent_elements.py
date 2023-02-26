class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        groups = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            groups[freq].append(num)

        result = []
        for i in range(len(groups) - 1, -1, -1):
            if len(result) < k:
                result.extend(groups[i])

        return result
