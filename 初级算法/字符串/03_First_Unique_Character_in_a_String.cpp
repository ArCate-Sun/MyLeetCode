//
// First Unique Character in a String
//
// 要求:
// 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
//
// 示例 1:
// s = "leetcode"
// 返回 0.
//
// 示例 2:
// s = "loveleetcode",
// 返回 2.
//
// 注意事项:
// 您可以假定该字符串只包含小写字母。
//

#include <iostream>

using namespace std;

class Solution {
public:
    int firstUniqChar(string s) {

        int map[26] = {0};

        for (int i = 0; i < s.length(); ++i) {
            ++map[s[i] - 'a'];
        }
        for (int i = 0; i < s.length(); ++i) {
            if (map[s[i] - 'a'] == 1) return i;
        }

        return -1;
    }

};
