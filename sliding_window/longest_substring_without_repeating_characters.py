class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = set()
        
        l, longest = 0, 0
        for c in s:
            while c in unique_chars:
                unique_chars.remove(s[l])
                l += 1
            unique_chars.add(c)
            longest = max(longest, len(unique_chars))
        return longest