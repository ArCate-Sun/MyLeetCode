//
// Implement strStr()
//
// 要求:
// 实现 strStr()。
// 返回蕴含在 haystack 中的 needle 的第一个字符的索引，如果 needle 不是 haystack 的一部分则返回 -1 。
//
// 示例 1:
// 输入: haystack = "hello", needle = "ll"
// 输出: 2
//
// 示例 2:
// 输入: haystack = "aaaaa", needle = "bba"
// 输出: -1
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:

    int strStr(string haystack, string needle) {

        vector<int> next(needle.length());
        this->make_next(next, needle);

        return this->strStr(haystack, needle, next);
    }

private:

    int strStr(const string& haystack, const string& needle, const vector<int>& next) {

        if (next.empty()) return 0;

        int needle_i = next[0];
        for (int i = 0; i < haystack.length(); ++i) {

            if (haystack[i] == needle[needle_i + 1]) {
                ++needle_i;
                if (needle_i + 1 == needle.length()) {
                    return i - needle_i;
                }
            } else {
                if (needle_i < 0) {
                    needle_i = -1;
                } else {
                    needle_i = next[needle_i];
                    --i;
                }
            }

        }
        return -1;
    }

    int get_next_value(const vector<int>& next,const string& needle, const int idx) {

        if (idx == 0) {
            return -1;
        }

        for (int pre_idx = next[idx - 1]; ; pre_idx = next[pre_idx]) {
            if (needle[idx] == needle[pre_idx + 1]) {
                return pre_idx + 1;
            } else if (pre_idx == -1) {
                return -1;
            }
        }

    }

    void make_next(vector<int> &next, const string &needle) {

        long len = needle.length();
        if (len <= 0) {
            return;
        }

        for (int i = 0; i < len; ++i) {
            next[i] = this->get_next_value(next, needle, i);
        }

    }
};
