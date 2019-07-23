"""
Question:
	Generate Parentheses
See:
	https://leetcode.com/problems/generate-parentheses/
"""
from typing import Set, List

from common.verification import Verification


class Solution:
	parenthesis = {
		1: ["()"]
	}

	def generateParenthesis(self, n: int) -> List[str]:

		if n <= 0:
			return []

		if n in Solution.parenthesis:
			return Solution.parenthesis[n]

		tmp_parenthesis = [
			x + y
			for i in range(n)
			for x in self.generateParenthesis(i)
			for y in self.generateParenthesis(n - i)
		] + [
			"(%s)" % s for s in self.generateParenthesis(n - 1)
		]
		Solution.parenthesis[n] = list(set(tmp_parenthesis))
		return Solution.parenthesis[n]


if __name__ == "__main__":

	inputs = [
		3,
		4
	]
	targets = [
		[
			"((()))",
			"(()())",
			"(())()",
			"()(())",
			"()()()"
		],
		[
			"(((())))",
			"((()()))",
			"((())())",
			"((()))()",
			"(()(()))",
			"(()()())",
			"(()())()",
			"(())(())",
			"(())()()",
			"()((()))",
			"()(()())",
			"()(())()",
			"()()(())",
			"()()()()"
		]
	]

	s = Solution()
	answers = []
	for i in inputs:
		if type(i) == tuple:
			output = s.generateParenthesis(*i)
		else:
			output = s.generateParenthesis(i)
		answers.append(output)

	verification = Verification(inputs, answers, targets)
	verification.verify()