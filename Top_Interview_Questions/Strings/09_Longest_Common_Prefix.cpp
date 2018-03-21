//
// Longest Common Prefix
//
// Required:
// Write a function to find the longest common prefix string amongst an array of strings.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {

        if (strs.empty()) {
            return "";
        }

        string result;

        char c;
        int i = 0;
        while (true) {

            if (i >= strs[0].length()) {
                return result;
            } else {
                c = strs[0][i];
            }

            for (int j = 1; j < strs.size(); ++j) {
                if (i >= strs[j].length() || strs[j][i] != c) {
                    return result;
                } else {
                    c = strs[j][i];
                }
            }

            ++i;
            result.push_back(c);
        }
    }
};
