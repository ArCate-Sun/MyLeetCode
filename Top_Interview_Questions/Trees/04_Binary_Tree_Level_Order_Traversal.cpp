//
// Binary Tree Level Order Traversal
//
// Required:
// Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
//
// Example:
// Given binary tree [3,9,20,null,null,15,7],
//     3
//    / \
//   9  20
//     /  \
//    15   7
// return its level order traversal as:
// [
//  [3],
//  [9,20],
//  [15,7]
// ]
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
	vector<vector<int>> levelOrder(TreeNode* root) {

		vector<vector<int>> result;
		queue<TreeNode *> q;

		// 压入根节点
		if (root) q.push(root);

		while (!q.empty()) {

			vector<int> level;

			long len = q.size();
			for (int i = 0; i < len; ++i) {

				TreeNode* node = q.front();
				level.push_back(node->val);
				q.pop();

				if (node->left) {
					q.push(node->left);
				}
				if (node->right) {
					q.push(node->right);
				}

			}

			result.push_back(level);
		}

		return result;
	}
};

