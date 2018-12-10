"""
Question:
	Valid Palindrome
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/
"""
import string
import re


class Solution:
	def isPalindrome(self, s):
		"""
		:type s: str
		:rtype: bool
		"""

		s = s.lower()
		pure_s = re.sub("[^a-z0-9]", "", s)
		return pure_s == pure_s[::-1]

	def isPalindrome2(self, s):
		"""
		:type s: str
		:rtype: bool
		"""

		alpha_list = [c.lower() for c in s if c in (string.digits + string.ascii_letters)]
		for i in range(len(alpha_list) // 2):
			if alpha_list[i] != alpha_list[-i - 1]:
				return False
		return True

	def isPalindrome3(self, s):
		"""
		:type s: str
		:rtype: bool
		"""

		alpha_set = set(list(string.digits) + list(string.ascii_letters))
		l, r = 0, len(s) - 1
		while l < r:
			if s[l] not in alpha_set:
				l += 1
			elif s[r] not in alpha_set:
				r -= 1
			elif s[l].lower() != s[r].lower():
				return False
			else:
				l += 1
				r -= 1
		return True


if __name__ == "__main__":
	s = Solution()

	input = "A man, a plan, a canal: Panama"
	print("Input: %s" % input)
	output = s.isPalindrome(input)
	print("Output: %s" % output)

	input = "race a car"
	print("Input: %s" % input)
	output = s.isPalindrome(input)
	print("Output: %s" % output)
