//
// Move Zeroes
//
// Required:
// Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
//
// Example:
// Given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
//
// Note:
// You must do this in-place without making a copy of the array.
// Minimize the total number of operations.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void moveZeroes(vector<int> &nums) {

        if (nums.empty()) return;

        int zero_count = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == 0) {
                ++zero_count;
            }
            if (zero_count && nums[i]) {
                nums[i - zero_count] = nums[i];
            }
        }

        // 将剩下的元素置为 0
        for (auto iter = nums.end() - zero_count; iter < nums.end(); ++iter) {
            *iter = 0;
        }

    }
};
