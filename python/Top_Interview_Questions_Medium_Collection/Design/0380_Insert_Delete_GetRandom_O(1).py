"""
Question:
	Serialize and Deserialize Binary Tree
See:
	https://leetcode.com/problems/serialize-and-deserialize-binary-tree
"""
import random


class RandomizedSet:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.data = []
		self.idxs = {}

	def insert(self, val: int) -> bool:
		"""
		Inserts a value to the set. Returns true if the set did not already contain the specified element.
		"""
		if val not in self.idxs:
			self.data.append(val)
			self.idxs[val] = len(self.data) - 1
			return True
		else:
			return False

	def remove(self, val: int) -> bool:
		"""
		Removes a value from the set. Returns true if the set contained the specified element.
		"""
		if val in self.idxs:
			self.idxs[self.data[-1]] = self.idxs[val]
			self.data[self.idxs.pop(val)] = self.data[-1]
			self.data.pop()
			return True
		else:
			return False

	def getRandom(self) -> int:
		"""
		Get a random element from the set.
		"""
		return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

if __name__ == "__main__":
	val = 2
	obj = RandomizedSet()
	param_1 = obj.insert(val)
	param_2 = obj.remove(val)
	param_3 = obj.getRandom()
