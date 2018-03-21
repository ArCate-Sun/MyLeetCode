//
// Single Number
//
// Required
// Given an array of integers, every element appears twice except for one. Find that single one.
//
// Note:
// Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
//


#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int singleNumber(vector<int> &nums) {

        if (nums.empty()) {
            return 0;
        }
        if (nums.size() == 1) {
            return nums[0];
        }

        vector<int> asc(nums);

        sort(asc.begin(), asc.end());

        // 扫描到只出现一项的元素
        for (int i = 0; i < asc.size() - 1; i += 2) {
            cout << asc[i] << endl;
            if(asc[i] != asc[i + 1]) return asc[i];
        }
        return asc[asc.size() - 1];
    }
};