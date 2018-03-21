//
// Reverse Integer
//
// Required:
// Given a 32-bit signed integer, reverse digits of an integer.
//
// Example 1:
// Input: 123
// Output:  321

// Example 2:
// Input: -123
// Output: -321
//
// Example 3:
// Input: 120
// Output: 21
//
// Note:
// Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range.
// For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
//

#include <iostream>

using namespace std;

class Solution {
public:
    int reverse(int x) {

        long result = 0;
        bool isNegtive = x < 0;

        if (isNegtive) {
            x = -x;
        }

        // 计算 x 的长度
        int x_len;
        int tmp = x;
        for (int i = 0; ; ++i) {
            if (!(tmp /= 10)) {
                x_len = i + 1;
                break;
            }
        }

        // 从低位依次取出 x 的每一位数, 加到 result 中
        for (int i = 0; i < x_len; ++i) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        result = isNegtive ? - result : result;

        return result > INT_MIN && result < INT_MAX ? (int) result : 0;
    }
};
