//
// Valid Anagram
//
// 要求:
// 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。
//
// 示例:
// s = "anagram"，t = "nagaram"，返回 true
// s = "rat"，t = "car"，返回 false
//
// 注意:
// 假定字符串只包含小写字母。
//
// 提升难度:
// 输入的字符串包含 unicode 字符怎么办？你能能否调整你的解法来适应这种情况？
//

#include <iostream>

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {

        if (s.length() != t.length()) return false;

        int map[26] = {0};

        for (char i : s) {
            ++map[i - 'a'];
        }
        for (char i : t) {
            --map[i - 'a'];
        }

        for (int i : map) {
            if (i != 0) return false;
        }

        return true;
    }
};
