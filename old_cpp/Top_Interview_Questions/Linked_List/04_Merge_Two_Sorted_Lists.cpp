//
// Merge Two Sorted Lists
//
// Required:
// Merge two sorted linked lists and return it as a new list.
// The new list should be made by splicing together the nodes of the first two lists.
//
// Example:
// Input: 1->2->4, 1->3->4
// Output: 1->1->2->3->4->4


struct ListNode {
    int val;
    ListNode *next;

    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {

        // 建立带头节点的排序链表
        ListNode *head = new ListNode(0);
        ListNode *end = head;

        ListNode *iter1 = l1;
        ListNode *iter2 = l2;
        while (iter1 && iter2) {

            // 取两个迭代变量指的节点中所包含的最小的值
            // 并使包含最小值的节点的迭代器指向后续的一个节点
            int value;
            if (iter1->val < iter2->val) {
                value = iter1->val;
                iter1 = iter1->next;
            } else {
                value = iter2->val;
                iter2 = iter2->next;
            }

            // 找到的将最小值追加到排序链表中的末尾
            end = end->next = new ListNode(value);

        }

        ListNode *iter = iter1 ? iter1 : iter2;
        while (iter) {
            end->next = new ListNode(iter->val);
            end = end->next;
            iter = iter->next;
        }

        // 删除排序列表的头结点
        ListNode *temp = head;
        head = head->next;
        delete temp;

        return head;
    }
};