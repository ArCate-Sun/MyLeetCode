"""
Question:
	String to Integer (atoi)
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/
"""


class Solution(object):
	def myAtoi(self, string):
		"""
		:type string: str
		:rtype: int
		"""

		number_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

		# 数字开始的位置
		num_start_idx = 0
		# 是否是负数
		is_negative = False

		# 越过空格
		for c in string:
			if c == " ":
				num_start_idx += 1
			else:
				break

		# 判断正负号
		if len(string) > num_start_idx:
			if string[num_start_idx] == "+":
				num_start_idx += 1
			elif string[num_start_idx] == "-":
				is_negative = True
				num_start_idx += 1

		result = 0
		for i in range(num_start_idx, len(string)):
			if string[i] in number_chars:
				result = result * 10 + int(string[i])
			else:
				break

		if is_negative:
			result = -result

		max_int = 2147483647
		min_int = -2147483648
		if result > max_int:
			result = max_int
		elif result < min_int:
			result = min_int

		return result


if __name__ == "__main__":
	s = Solution()

	input = "42"
	print("Input: %s" % input)
	output = s.myAtoi(input)
	print("Output: %s" % output)

	input = "   -42"
	print("Input: %s" % input)
	output = s.myAtoi(input)
	print("Output: %s" % output)

	input = "4193 with words"
	print("Input: %s" % input)
	output = s.myAtoi(input)
	print("Output: %s" % output)

	input = "words and 987"
	print("Input: %s" % input)
	output = s.myAtoi(input)
	print("Output: %s" % output)

	input = "-91283472332"
	print("Input: %s" % input)
	output = s.myAtoi(input)
	print("Output: %s" % output)