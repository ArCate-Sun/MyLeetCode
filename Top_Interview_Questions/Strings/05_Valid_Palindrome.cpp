//
// Valid Palindrome
//
// Required:
// Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
//
// Example:
// "A man, a plan, a canal: Panama" is a palindrome.
// "race a car" is not a palindrome.
//
// Note:
// Have you consider that the string might be empty?
// This is a good question to ask during an interview.
// For the purpose of this problem, we define empty string as valid palindrome.
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

        // 若 s 仅剩 1 位字符, 则判断为回文
        if (s.length() == 1) return true;

        // 从两边向中间依次比较每位字符是否相等
        for (int i = 0; i < s.length() / 2; ++i) {
            if (s[i] != s[s.length() - i - 1]) return false;
        }

        return true;
    }
};
