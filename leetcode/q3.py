class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)

        longest = 0 # Base case empty str
        for i in range(length):
            substr = s[i]
            longest = max(1, longest) # Incase ex. "bbbbb"
            for j in range(i + 1, length):
                char = s[j]
                if char not in substr:
                    substr += char
                    longest = max(len(substr), longest)
                else:
                    break

        return longest

print(Solution().lengthOfLongestSubstring("bbbbb"))
