//
// Intersection of Two Arrays II
//
// 要求:
// 给定两个数组，写一个方法来计算它们的交集。
//
// 示例:
// 给定 nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2, 2].
//
// 注意:
// 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
// 我们可以不考虑输出结果的顺序。
//
// 跟进:
// 如果给定的数组已经排好序呢？你将如何优化你的算法？
// 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
// 如果nums2的元素存储在磁盘上，内存是有限的，你不能一次加载所有的元素到内存中，你该怎么办？
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {

        // 排序
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());

        vector<int> result;

        // 计算合集元素并加入 result 中
        int i1 = 0;
        int i2 = 0;
        while (i1 < nums1.size() && i2 < nums2.size()) {
            if (nums1[i1] < nums2[i2]) {
                ++i1;
            } else if (nums1[i1] > nums2[i2]) {
                ++i2;
            } else {
                result.push_back(nums1[i1]);
                ++i1;
                ++i2;
            }
        }

        return result;
    }
};