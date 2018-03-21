//
// Two Sum
//
// 要求:
// 给定一个整数数列，找出其中和为特定值的那两个数。
// 你可以假设每个输入都只会有一种答案，同样的元素不能被重用。
//
// 示例:
// 给定 nums = [2, 7, 11, 15], target = 9
// 因为 nums[0] + nums[1] = 2 + 7 = 9
// 所以返回 [0, 1]
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target) {

        vector<int> result;

        if (nums.size() < 2) {
            return result;
        }

        vector<int> asc(nums);
        sort(asc.begin(), asc.end());
        for (int i = 0; i < asc.size(); ++i) {
            for (int j = i + 1; j < asc.size() || asc[i] + asc[j] > target; ++j) {

                if (asc[i] + asc[j] == target) {
                    int targets[] = {asc[i], asc[j]};
                    return findElementsPosition(nums, targets, 2);
                }
            }
        }

        return result;
    }

    vector<int> findElementsPosition(vector<int> &nums, const int *targets, int targets_num) {
        vector<int> result;

        vector<int> temp(nums);
        for (int i = 0; i < targets_num; ++i) {
            for (int j = 0; j < temp.size(); ++j) {
                if (temp[j] == targets[i] && !this->contain(result, j)) {
                    result.push_back(j);
                    break;
                }
            }
        }

        return result;
    }

    bool contain(vector<int> &nums, int target) {
        for (auto &&item : nums) {
            if (item == target) {
                return true;
            }
        }
        return false;
    }
};
