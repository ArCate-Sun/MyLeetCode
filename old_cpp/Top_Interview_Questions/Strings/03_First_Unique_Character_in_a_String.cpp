//
// First Unique Character in a String
//
// Required:
// Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
//
// Example 1:
// s = "leetcode"
// return 0.
//
// Example 2:
// s = "loveleetcode",
// return 2.
//
// Note:
// You may assume the string contain only lowercase letters.
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
