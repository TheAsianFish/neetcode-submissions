class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        left = 0
        letters = defaultdict(int)
        for right in range(len(s)):
            while s[right] in letters:
                del letters[s[left]] 
                left += 1
            letters[s[right]] += 1
            best = max(best, right - left + 1)
        return best