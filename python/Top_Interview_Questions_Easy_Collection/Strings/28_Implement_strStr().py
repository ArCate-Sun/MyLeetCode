"""
Question:
	Implement strStr()
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/
"""


class Solution:
	def strStr(self, haystack, needle):
		"""
		:type haystack: str
		:type needle: str
		:rtype: int
		"""

		if haystack == needle == "":
			return 0

		for i in range(len(haystack) - len(needle) + 1):
			if haystack[i : i + len(needle)] == needle:
				return i
		return -1


if __name__ == "__main__":
	s = Solution()

	haystack = "hello"
	needle = "ll"
	print("Input: haystack = %s, needle = %s" % (haystack, needle))
	output = s.strStr(haystack, needle)
	print("Output: %s" % output)

	haystack = "aaaaa"
	needle = "bba"
	print("Input: haystack = %s, needle = %s" % (haystack, needle))
	output = s.strStr(haystack, needle)
	print("Output: %s" % output)
