"""
Question:
	Contains Duplicate
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/
"""
import string


class Solution:
	def isAnagram(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""

		if len(s) != len(t):
			return False

		for c in string.ascii_lowercase:
			if s.count(c) != t.count(c):
				return False
		return True


if __name__ == "__main__":
	sol = Solution()

	s = "anagram"
	t = "nagaram"
	print("Input: s = %s, t = %s" % (s, t))
	output = sol.isAnagram(s, t)
	print("Output: %s" % output)

	s = "rat"
	t = "car"
	print("Input: s = %s, t = %s" % (s, t))
	output = sol.isAnagram(s, t)
	print("Output: %s" % output)
