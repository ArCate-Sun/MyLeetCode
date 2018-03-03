//
// Contains Duplicate
//
// 要求:
// 给定一个整数数组，判断是否存在重复元素。
// 如果任何值在数组中出现至少两次，函数应该返回 true。如果每个元素都不相同，则返回 false。
//


#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int> &nums) {

        if (nums.size() <= 1) {
            return false;
        }

        vector<int> asc(nums);

        sort(asc.begin(), asc.end());

        // 判断相邻的两项是否相同
        for (int i = 0; i < asc.size() - 1; ++i) {
            if (asc[i] == asc[i + 1]) return true;
        }

        return false;
    }
};