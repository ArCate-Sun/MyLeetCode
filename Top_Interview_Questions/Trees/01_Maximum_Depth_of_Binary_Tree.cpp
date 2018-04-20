//
// Maximum Depth of Binary Trees
//
// Required:
// Given a binary tree, find its maximum depth.
// The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
//
// Example:
// Given binary tree [3,9,20,null,null,15,7],
//     3
//    / \
//   9  20
//     /  \
//    15   7
// return its depth = 3.
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
    int maxDepth(TreeNode* root) {

        if (!root) return 0;
        if (!root->left && !root->right) return 1;

        int l = this->maxDepth(root->left);
        int r = this->maxDepth(root->right);

        return max(r, l) + 1;
    }
};
