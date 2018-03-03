//
// Remove Duplicates from Sorted Array
//
// 要求:
// 给定一个有序数组，你需要原地删除其中的重复内容，使每个元素只出现一次,并返回新的长度。
// 不要另外定义一个数组，您必须通过用 O(1) 额外内存原地修改输入的数组来做到这一点。
//
// 示例：
// 给定数组: nums = [1,1,2],
// 你的函数应该返回新长度 2, 并且原数组nums的前两个元素必须是1和2
// 不需要理会新的数组长度后面的元素
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
