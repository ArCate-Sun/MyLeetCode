//
// Plus One
//
// 要求:
// 给定一个非负整数组成的非空数组，给整数加一。
// 可以假设整数不包含任何前导零，除了数字0本身。
// 最高位数字存放在列表的首位。
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {

        if (digits.empty()) return digits;

        vector<int> result(digits);

        int first = result[0];
        for (auto iter = result.end() - 1; iter >= result.begin(); --iter) {
            if (*iter < 9) {
                ++ *iter;
                break;
            } else {
                *iter = 0;
            }
        }

        // 如果数组的最初第 0 位为 9, 而现在第 0 位为 0, 则数组第 0 位必然进位, 则需在数组最初插入元素 1
        if (first == 9 && result[0] == 0) {
            result.insert(result.begin(), 1);
        }

        return result;
    }
};
