class Solution:
    # uses i,j pointers and dynamic sliding window technique
    # Time Complexity: O(n)
    # Space Complexity: O(min(m,n)) ...where m is size of the window
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest_length = 0  # defaulting to 0 for empty string case
        i = 0
        char_index_map = {}  # stores the new start value if element is found again

        for j in range(n):
            if s[j] in char_index_map:
                i = max(char_index_map[s[j]], i)

            longest_length = max(longest_length, j - i + 1)
            char_index_map[s[j]] = j + 1

        return longest_length


s = Solution()
print(s.lengthOfLongestSubstring("dvdf"))
