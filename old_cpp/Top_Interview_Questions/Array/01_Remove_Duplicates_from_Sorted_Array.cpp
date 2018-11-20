//
// Remove Duplicates from Sorted Array
//
// Required:
// Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.
// Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
//
// Example:
// Given nums = [1,1,2],
// Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
// It doesn't matter what you leave beyond the new length.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int> &nums) {

        // 判断 nums 为空
        if (nums.empty()) {
            return 0;
        }

        auto iter_curr = nums.begin();
        iter_curr;
        auto iter_idx = nums.begin();
        ++iter_idx;

        // 原地删除重复内容
        for (; iter_idx != nums.end(); ++iter_idx) {
            if (*iter_curr != *iter_idx) {
                if (iter_curr != iter_idx - 1) {
                    *(iter_curr + 1) = *iter_idx;
                }
                ++iter_curr;
            }
        }

        // 删除多余内容
        nums.erase(iter_curr + 1, nums.end());

        return nums.size();
    }
};
