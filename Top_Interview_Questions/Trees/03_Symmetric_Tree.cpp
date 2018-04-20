//
// Symmetric Tree
//
// Required:
// Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
//
// Example 1:
// This binary tree [1,2,2,3,4,4,3] is symmetric:
//     1
//    / \
//   2   2
//  / \ / \
// 3  4 4  3
//
// Example 2:
// The following [1,2,2,null,3,null,3] is not:
//     1
//    / \
//   2   2
//    \   \
//     3   3
//
// Note:
// Bonus points if you could solve it both recursively and iteratively.
//

#include <iostream>
using namespace std;

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
	bool isMirror(TreeNode* left, TreeNode* right) {

		if (!left && !right) return true;
		else if (!left || !right) return false;

		if (left->val == right->val)
			return this->isMirror(left->left, right->right) && this->isMirror(left->right, right->left);
		else
			return false;
	}

	bool isSymmetric(TreeNode* root) {

		if (!root) return true;

		return this->isMirror(root->left, root->right);
	}
};
