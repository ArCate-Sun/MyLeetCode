"""
Question:
	Longest Substring Without Repeating Characters
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/779/
"""


class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:

		if not s:
			return 0

		max_sub_len = 0
		idx_start = 0
		char_to_index = {}
		for i, c in enumerate(s):     
			if c in char_to_index and char_to_index[c] >= idx_start:
				max_sub_len = max(max_sub_len, i - idx_start)
				idx_start = char_to_index[c] + 1
			char_to_index[c] = i

		max_sub_len = max(max_sub_len, i - idx_start + 1)

		return max_sub_len

	def lengthOfLongestSubstring2(self, s: str) -> int:

		if not s:
			return 0

		s += "."
		max_sub_len = 0
		idx_start = 0
		for i in range(1, len(s)):
			if s[i] in s[idx_start : i]:
				max_sub_len = max(max_sub_len, i - idx_start)
				idx_start = s[idx_start : i].rfind(s[i]) + 1 + idx_start
		max_sub_len = max(max_sub_len, i - idx_start)
		return max_sub_len

if __name__ == "__main__":

	demos = [
		"1",
		"au",
		"dvdf",
		"abcabcbb",
		"bbbbbbbbbb",
		"pwwkew",
	]
	results = [
		1,
		2,
		3,
		3,
		1,
		3
	]

	s = Solution()
	for demo, result in zip(demos, results):

		if type(demo) == tuple:
			output = s.lengthOfLongestSubstring(*demo)
		else:
			output = s.lengthOfLongestSubstring(demo)

		print("INPUT: %s" % str(demo))
		if output == result:
			print("\033[0;32mOUTPUT: %s\033[0m" % str(output))
		else:
			print("\033[0;31mOUTPUT: %s\033[0m" % str(output))
			print("\033[0;36mEXPECT: %s\033[0m" % str(result))
		print()
