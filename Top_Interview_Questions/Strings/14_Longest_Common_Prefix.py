"""
Question:
	Longest Common Prefix
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/
"""


class Solution:

	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""

		if not strs:
			return ""

		for i, words in enumerate(zip(*strs)):
			if len(set(words)) > 1:
				return strs[0][:i]
		else:
			return min(strs)

	def is_common_prefix(self, prefix, strs):
		"""
		指定字符串是否字符串列表中的共同前缀
		:param prefix:
		:param strs:
		:return:
		"""
		for str in strs:
			if str[:len(prefix)] != prefix:
				return False
		return True

	def longestCommonPrefix2(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""

		if not strs:
			return ""

		# 找最短字符串
		shortest_str = strs[0]
		for str in strs:
			if len(shortest_str) > len(str):
				shortest_str = str

		l, r = 0, len(shortest_str)
		prefix_length = (l + r) // 2
		while l <= r:
			tmp_prefix = shortest_str[:prefix_length]
			print(tmp_prefix, l, r)

			if self.is_common_prefix(tmp_prefix, strs):
				l = prefix_length + 1
			else:
				r = prefix_length - 1
			prefix_length = (l + r) // 2

		return shortest_str[:prefix_length]


if __name__ == "__main__":
	s = Solution()

	input = ["flower", "flow", "flight"]
	print("Input: %s" % input)
	output = s.longestCommonPrefix(input)
	print("Output: %s" % output)

	input = ["dog", "racecar", "car"]
	print("Input: %s" % input)
	output = s.longestCommonPrefix(input)
	print("Output: %s" % output)

	input = ["aab"]
	print("Input: %s" % input)
	output = s.longestCommonPrefix(input)
	print("Output: %s" % output)
