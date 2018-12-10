"""
Question:
	Min Stack
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/562/
"""


class MinStack:

	_stack = None
	_min = None

	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self._stack = []

	def push(self, x):
		"""
		:type x: int
		:rtype: void
		"""
		self._stack.append(x)
		if self._min is None:
			self._min = min(self._stack)
		elif self._min > x:
			self._min = x

	def pop(self):
		"""
		:rtype: void
		"""
		if self._min == self._stack[-1]:
			self._min = None
		return self._stack.pop()

	def top(self):
		"""
		:rtype: int
		"""
		return self._stack[-1]

	def getMin(self):
		"""
		:rtype: int
		"""
		if self._min is not None:
			return self._min
		return min(self._stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == "__main__":
	minStack = MinStack()
	minStack.push(-2)
	minStack.push(0)
	minStack.push(-20)
	output = minStack.getMin()  # Returns - 3
	print(output)
	minStack.pop()
	minStack.push(-7)
	output = minStack.getMin()  # Returns - 3
	print(output)
	output = minStack.top()  # Returns 0
	print(output)
	output = minStack.getMin()  # Returns - 2
	print(output)
