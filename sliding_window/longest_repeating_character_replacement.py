class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l, longest, most_freq = 0, 0, 0

        for r, c in enumerate(s):
            count[c] += 1
            most_freq = max(most_freq, count[c])

            if (r - l + 1) - most_freq > k:
                count[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)

        return longest
