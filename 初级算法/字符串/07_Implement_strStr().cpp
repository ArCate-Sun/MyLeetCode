//
// Implement strStr()
//
// Required:
// Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
//
// Example 1:
// Input: haystack = "hello", needle = "ll"
// Output: 2
//
// Example 2:
// Input: haystack = "aaaaa", needle = "bba"
// Output: -1
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
