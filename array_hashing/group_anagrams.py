class Solution:
    def count(self, s):
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        return count

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            groups[tuple(self.count(s))].append(s)
        
        return groups.values()