//
// Valid Palindrome
//
// 要求:
// 给定一个字符串，确定它是否是回文，只考虑字母数字字符和忽略大小写。
//
// 例如:
// "A man, a plan, a canal: Panama" 是回文字符串。
// "race a car" 不是回文字符串。
//
// 注意:
// 你有考虑过这个字符串可能是空的吗？ 在面试中这是一个很好的问题。
// 针对此题目，我们将空字符串定义为有效的回文字符串。
//

#include <iostream>

using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {

        // 将 s 中大写字母转为小写, 并除去 s 中的数字, 字符和空格
        int curr = 0;
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] >= 'A' && s[i] <= 'Z') {
                // 如果是大写字母
                s[curr] = 'a' + s[i] - 'A';
                ++curr;
            } else if (s[i] >= 'a' && s[i] <= 'z') {
                // 如果是小写字母
                if (curr != i) s[curr] = s[i];
                ++curr;
            } else if (s[i] >= '0' && s[i] <= '9') {
                // 如果是数字
                if (curr != i) s[curr] = s[i];
                ++curr;
            }
        }
        s.erase(curr, s.length());

        // 若 s 仅剩 1 位字符, 则判断不为回文
        if (s.length() == 1) return false;

        // 从两边向中间依次比较每位字符是否相等
        for (int i = 0; i < s.length() / 2; ++i) {
            if (s[i] != s[s.length() - i - 1]) return false;
        }

        return true;
    }
};
