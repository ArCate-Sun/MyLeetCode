"""
Question:
	Longest Palindromic Substring
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/780/
"""


class Solution:
	def longestPalindrome(self, s: str) -> str:

		"""Manacher Algorithm 马拉车算法"""

		if not s:
			return ""

		longest_len = 0
		center = 0

		mx = id = 0
		s2 = "$#" + "#".join(s) + "#%"
		p = [1] * len(s2)
		for i in range(1, len(s2) - 1):
			if mx > i:
				j = 2 * id - i
				p[i] = min(p[j], mx - i)

			while s2[i + p[i]] == s2[i - p[i]]:
				p[i] += 1

			if mx < i + p[i]:
				mx = i + p[i]
				id = i

			if longest_len < p[i]:
				longest_len = p[i]
				center = i

		left = (center - longest_len) // 2
		right = left + longest_len - 1
		return s[left : right]


if __name__ == "__main__":

	demos = [
		"babad",
		"cbbd"
	]
	results = [
		"bab",
		"bb"
	]

	s = Solution()
	for demo, result in zip(demos, results):

		if type(demo) == tuple:
			output = s.longestPalindrome(*demo)
		else:
			output = s.longestPalindrome(demo)

		print("INPUT: %s" % str(demo))
		if output == result:
			print("\033[0;32mOUTPUT: %s\033[0m" % str(output))
		else:
			print("\033[0;31mOUTPUT: %s\033[0m" % str(output))
			print("\033[0;36mEXPECT: %s\033[0m" % str(result))
		print()
