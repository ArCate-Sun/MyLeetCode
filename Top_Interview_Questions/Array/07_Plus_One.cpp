//
// Plus One
//
// Required:
// Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
// You may assume the integer do not contain any leading zero, except the number 0 itself.
// The digits are stored such that the most significant digit is at the head of the list.
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
