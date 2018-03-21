//
// Contains Duplicate
//
// 要求:
// Given an array of integers, find if the array contains any duplicates.
// Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
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