//
// Valid Anagram
//
// Required:
// Given two strings s and t, write a function to determine if t is an anagram of s.
//
// Example:
// s = "anagram", t = "nagaram", return true.
// s = "rat", t = "car", return false.
//
// Note:
// You may assume the string contains only lowercase alphabets.
//
// Follow up:
// What if the inputs contain unicode characters? How would you adapt your solution to such case?
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
