"""
Question:
	Letter Combinations of a Phone Number
See:
	https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
from typing import List


class Solution:
	n2c = {
		"2": ["a", "b", "c"],
		"3": ["d", "e", "f"],
		"4": ["g", "h", "i"],
		"5": ["j", "k", "l"],
		"6": ["m", "n", "o"],
		"7": ["p", "q", "r", "s"],
		"8": ["t", "u", "v"],
		"9": ["w", "x", "y", "z"]
	}

	def letterCombinations(self, digits: str) -> List[str]:

		def helper(combination: str, digits: str):
			if not digits:
				result.append(combination)
			else:
				for c in Solution.n2c[digits[0]]:
					helper(combination + c, digits[1:])

		result = []
		if digits:
			helper("", digits)
		return result


if __name__ == "__main__":

	def judge_answer(answer, target):

		if type(answer) != type(target):
			return False

		if type(target) == set:
			return not answer.symmetric_difference(target)

		if type(target) == list:
			return sorted(answer) == sorted(target)

		if type(target) == dict:
			for k in target.keys():
				if answer[k] != target[k]:
					return False
		return True


	demos = [
		"23"
	]
	results = [
		["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
	]

	s = Solution()
	for demo, result in zip(demos, results):

		if type(demo) == tuple:
			output = s.letterCombinations(*demo)
		else:
			output = s.letterCombinations(demo)

		print("INPUT: %s" % str(demo))
		if judge_answer(output, result):
			print("\033[0;32mOUTPUT: %s\033[0m" % str(output))
		else:
			print("\033[0;31mOUTPUT: %s\033[0m" % str(output))
			print("\033[0;36mEXPECT: %s\033[0m" % str(result))
		print()
