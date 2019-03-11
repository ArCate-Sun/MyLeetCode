"""
Question:
	Group Anagrams
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/778/
"""


class Solution:
	def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
		"""
		:type strs: List[str]
		:rtype: List[List[str]]
		"""
		chars_dict = {}
		for s in strs:
			key = "".join(sorted(s))
			chars_dict.setdefault(key, []).append(s)
		return list(chars_dict.values())


if __name__ == "__main__":

	demos = [
		["eat", "tea", "tan", "ate", "nat", "bat"],
	]
	results = [
		[
			["ate", "eat", "tea"],
			["nat", "tan"],
			["bat"]
		]
	]

	s = Solution()
	for demo, result in zip(demos, results):

		if type(demo) == tuple:
			output = s.groupAnagrams(*demo)
		else:
			output = s.groupAnagrams(demo)

		print("INPUT: %s" % str(demo))
		if output == result:
			print("\033[0;32mOUTPUT: %s\033[0m" % str(output))
		else:
			print("\033[0;31mOUTPUT: %s\033[0m" % str(output))
			print("\033[0;36mEXPECT: %s\033[0m" % str(result))
		print()
