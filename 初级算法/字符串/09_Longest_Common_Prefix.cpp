//
// Longest Common Prefix
//
// 要求:
// 编写一个函数来查找字符串数组中最长的公共前缀字符串。
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
