//
// Move Zeroes
//
// 要求:
// 给定一个数组 nums, 编写一个函数将所有 0 移动到它的末尾，同时保持非零元素的相对顺序。
//
// 示例:
// 定义 nums = [0, 1, 0, 3, 12]，调用函数之后， nums 应为 [1, 3, 12, 0, 0]。
//
// 注意事项:
// 1. 必须在原数组上操作，不要为一个新数组分配额外空间。
// 2. 尽量减少操作总数。
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

int main() {

    int array[] = {
            0, 1, 0, 3, 12
    };

    vector<int> nums(array, array + sizeof(array) / sizeof(int));

    Solution solution;
    solution.moveZeroes(nums);

    for (int i = 0; i < nums.size(); i++) {
        cout << nums[i] << " ";
    }

    return 0;
}
