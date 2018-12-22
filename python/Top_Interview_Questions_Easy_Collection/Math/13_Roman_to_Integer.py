"""
Question:
	Roman to Integer
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/878/
"""


class Solution:
	def romanToInt(self, s):
		"""
		:type s: str
		:rtype: int
		"""

		char_to_value = {
			"M": 1000,
			"D": 500,
			"C": 100,
			"L": 50,
			"X": 10,
			"V": 5,
			"I": 1
		}

		result = 0
		max_char_value = 0
		for char in reversed(s):
			value = char_to_value[char]
			if value < max_char_value:
				result -= value
			else:
				result += value
				max_char_value = value

		return result


	def romanToInt2(self, s):
		"""
		:type s: str
		:rtype: int
		"""

		char_to_value = {
			"M": 1000,
			"CM": 900,
			"D": 500,
			"CD": 400,
			"C": 100,
			"XC": 90,
			"L": 50,
			"XL": 40,
			"X": 10,
			"IX": 9,
			"V": 5,
			"IV": 4,
			"I": 1
		}

		result = 0
		i = 0
		while i < len(s):
			for char, value in char_to_value.items():
				if s[i:].startswith(char):
					result += value
					i += len(char)
					break

		return result

	def romanToInt3(self, s):
		"""
		:type s: str
		:rtype: int
		"""

		s = s.replace("CM", "900 ").replace("M", "1000 ")\
			.replace("CD", "400 ").replace("D", "500 ")\
			.replace("XC", "90 ").replace("C", "100 ")\
			.replace("XL", "40 ").replace("L", "50 ")\
			.replace("IX", "9 ").replace("X", "10 ")\
			.replace("IV", "4 ").replace("V", "5 ")\
			.replace("I", "1 ")

		result = 0
		for c in s.split(" ")[:-1]:
			result += int(c)
		return result


if __name__ == "__main__":
	demos = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
	s = Solution()

	for demo in demos:
		input = demo
		print("INPUT: %s" % input)
		output = s.romanToInt(input)
		print("OUTPUT: %s" % output)
