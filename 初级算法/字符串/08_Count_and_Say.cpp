//
// Count and Say
//
// 要求:
// 数数并说序列是一个整数序列，第二项起每一项的值为对前一项的计数，其前五项如下：
// 1.     1
// 2.     11
// 3.     21
// 4.     1211
// 5.     111221
// 1 被读作 "一个一" 即 11。
// 11 被读作  "两个一" 即 21。
// 21 被读作  "一个二 和 一个一" 即 1211。
// 给一个正整数 n ，输出数数并说序列的第 n 项。
//
// 注意:
// 该整数序列的每项都输出为字符串。
//
// 示例 1:
// 输入: 1
// 输出: "1"
//
// 示例 2:
// 输入: 4
// 输出: "1211"
//

#include <iostream>

using namespace std;

class Solution {
public:
    string countAndSay(int n) {

        string result = "1";
        for (int i = 1; i < n; ++i) {
            result = this->countAndSay(result);
        }
        return result;
    }

private:
    string countAndSay(const string& str) {

        string result;

        int count = 1;
        char c = str[0];
        for (int i = 1; i < str.length(); ++i) {

            if (str[i] == c) {
                ++count;
            } else {

                result.push_back((char) count + '0');
                result.push_back(c);

                count = 1;
                c = str[i];
            }
        }
        result.push_back((char) count + '0');
        result.push_back(c);

        return result;
    }
};
