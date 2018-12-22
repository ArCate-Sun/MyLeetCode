"""
Question:
	Reverse Strings
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/
"""


class Solution:
	def reverseString(self, s):
		"""
		:type s: str
		:rtype: str
		"""

		return s[::-1]


if __name__ == "__main__":
	s = Solution()

	input = "hello"
	print("Input: %s" % input)
	output = s.reverseString(input)
	print("Output: %s" % output)

	input = "A man, a plan, a canal: Panama"
	print("Input: %s" % input)
	output = s.reverseString(input)
	print("Output: %s" % output)
