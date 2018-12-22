"""
Question:
	Valid Parentheses
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/721/
"""


class Solution:
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""

		parentheses = {
			"(": ")",
			"[": "]",
			"{": "}"
		}

		stack = []
		for c in s:
			if c in parentheses:
				stack.append(c)
			elif not stack:
				return False
			elif parentheses[stack[-1]] != c:
				return False
			else:
				stack.pop()
		return not stack


if __name__ == "__main__":

	demos = ["()", "()[]{}", "(]", "([)]", "{[]}"]
	results = [True, True, False, False, True]

	s = Solution()
	for demo, result in zip(demos, results):

		if type(demo) == tuple:
			output = s.isValid(*demo)
		else:
			output = s.isValid(demo)

		print("INPUT: %s" % str(demo))
		if output == result:
			print("\033[0;32mOUTPUT: %s\033[0m" % str(output))
		else:
			print("\033[0;31mOUTPUT: %s\033[0m" % str(output))
			print("\033[0;36mEXPECT: %s\033[0m" % str(result))
		print()
