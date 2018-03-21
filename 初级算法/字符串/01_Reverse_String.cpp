//
// Reverse String
//
// Required:
// Write a function that takes a string as input and returns the string reversed.
//
// Example:
// Given s = "hello", return "olleh".
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
