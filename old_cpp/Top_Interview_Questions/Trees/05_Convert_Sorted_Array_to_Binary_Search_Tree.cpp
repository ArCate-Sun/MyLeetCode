//
// Convert Sorted Array to Binary Search Tree
//
// Required:
// Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
// For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
//
// Example:
// Given the sorted array: [-10,-3,0,5,9],
// One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
//      0
//     / \
//   -3   9
//   /   /
// -10  5
//


#include <iostream>
#include <queue>
#include <vector>

using namespace std;

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;

	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
	TreeNode *sortedArrayToBST(vector<int> &nums) {
		return this->makeChildBST(nums, 0, nums.size() - 1);
	}

private:
	TreeNode *makeChildBST(vector<int> &nums, long begin, long end) {

		if (begin > end) return nullptr;

		long mid = (end - begin + 1) / 2 + begin;
		TreeNode *root = new TreeNode(nums[mid]);

		if (begin != end) {
			root->left = this->makeChildBST(nums, begin, mid - 1);
			root->right = this->makeChildBST(nums, mid + 1, end);
		}

		return root;
	}
};
