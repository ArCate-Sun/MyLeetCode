//
// Two Sum
//
// Required:
// Given an array of integers, return indices of the two numbers such that they add up to a specific target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
//
// Example:
// Given nums = [2, 7, 11, 15], target = 9,
// Because nums[0] + nums[1] = 2 + 7 = 9,
// return [0, 1].
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
