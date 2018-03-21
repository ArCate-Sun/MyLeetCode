//
// Reverse String
//
// 要求
// 请编写一个函数，其功能是将输入的字符串反转过来。
//
// 示例：
// 输入：s = "hello"
// 返回："olleh"
//

#include <iostream>

using namespace std;

class Solution {
public:
    string reverseString(string s) {
        int len = s.length();
        for (int i = 0; i < len / 2; ++i) {
            int x = len - i - 1;
            s[i] = s[i] + s[x];
            s[x] = s[i] - s[x];
            s[i] = s[i] - s[x];
        }
        return s;
    }
};
