//
// Palindrome Linked List
//
// Required:
// Given a singly linked list, determine if it is a palindrome.
//
// Follow up:
// Could you do it in O(n) time and O(1) space?
//

#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:

    /**
     * 反转链表
     * @param from  反转的起始节点
     * @param to    反转的终止节点
     * @return  true or false
     */
    bool reverseList(ListNode* from, ListNode* to) {

        if (!from || !to) return false;

        ListNode* curr = from;
        ListNode* next = curr->next;

        while (next) {
            ListNode* tmp = next->next;

            next->next = curr;

            curr = next;
            next = tmp;
        }

        from->next = nullptr;
        return true;
    }

    /**
     * 判断链表是否是回文
     * @param head  链表头节点
     * @return  true or false
     */
    bool isPalindrome(ListNode* head) {

        ListNode* end = head;
        ListNode* node;

        long len = 0;

        // 计算长度, 找到尾节点
        node = head;
        while (node) {
            ++len;
            end = node;
            node = node->next;
        }

        node = head;
        for (int i = 0; i < len / 2; ++i) {
            node = node->next;
        }

        // 反转链表中从 len/2 至 end 的部分
        this->reverseList(node, end);

        ListNode* lNode = head;
        ListNode* rNode = end;
        while (lNode != node) {
            cout << lNode->val << " " << rNode->val << endl;
            if (lNode->val != rNode->val) {
                return false;
            }
            lNode = lNode->next;
            rNode = rNode->next;
        }

        // 复原链表中的反转部分
        this->reverseList(end, node);

        return true;
    }
};
