"""
Question:
	First Unique Character in a String
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/
"""
import string


class Solution:
	def firstUniqChar(self, s):
		"""
		:type s: str
		:rtype: int
		"""

		first_unique_idx = len(s)
		for c in string.ascii_lowercase:
			l, r = s.find(c), s.rfind(c)
			if l != -1 and l < first_unique_idx and l == r:
				first_unique_idx = l
		return first_unique_idx if first_unique_idx != len(s) else -1

	def firstUniqChar2(self, s):
		"""
		:type s: str
		:rtype: int
		"""

		unique_indices = [s.find(c) for c in string.ascii_lowercase if s.count(c) == 1]
		return min(unique_indices) if len(unique_indices) > 0 else -1


if __name__ == "__main__":
	s = Solution()

	input = "leetcode"
	print("Input: %s" % input)
	output = s.firstUniqChar(input)
	print("Output: %s" % output)

	input = "loveleetcode"
	print("Input: %s" % input)
	output = s.firstUniqChar(input)
	print("Output: %s" % output)

