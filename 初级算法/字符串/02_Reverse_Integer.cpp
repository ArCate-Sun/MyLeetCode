//
// Reverse Integer
//
// 要求
// 给定一个范围为 32 位 int 的整数，将其颠倒。
//
// 示例 1:
// 输入: 123
// 输出:  321
//
// 示例 2:
// 输入: -123
// 输出: -321
//
// 示例 3:
// 输入: 120
// 输出: 21
//
// 注意:
// 假设我们的环境只能处理 32 位 int 范围内的整数。根据这个假设，如果颠倒后的结果超过这个范围，则返回 0。
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
