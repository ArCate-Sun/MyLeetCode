//
// Single Number
//
// 要求:
// 给定一个整数数组，除了某个元素外其余元素均出现两次。请找出这个只出现一次的元素。
//
// 备注：
// 你的算法应该是一个线性时间复杂度。 你可以不用额外空间来实现它吗？
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