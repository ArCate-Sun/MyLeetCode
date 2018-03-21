//
// Rotate Array
// Rotate an array of n elements to the right by k steps.
//
// Example:
// With n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
//
// Note:
// Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
//
// Hint:
// Could you do it in-place with O(1) extra space?
//
// Related problem:
// Reverse Words in a String II
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {

        if (nums.empty() || k < 0) return;

        for (int i = 0; i < k; ++i) {
            int temp = nums[nums.size() - 1];
            for (int j = nums.size() - 1; j > 0; --j) {
                nums[j] = nums[j - 1];
            }
            nums[0] = temp;
        }
    }
};