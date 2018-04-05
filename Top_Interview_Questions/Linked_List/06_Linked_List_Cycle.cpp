//
// Linked List Cycle
//
// Required:
// Given a linked list, determine if it has a cycle in it.
//
// Follow up:
// Can you solve it without using extra space?
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
     *
     * 判断链表中是否存在回链
     *
     * 思路: 设置快慢指针, 快慢指针以不同的速度找寻后继节点, 若有循环, 快慢必会相遇
     *
     * @param head
     * @return
     */
    bool hasCycle(ListNode *head) {
        ListNode *fNode = head;
        ListNode *sNode = head;

        while (fNode) {

            // 快指针多走一步
            fNode = fNode->next;
            if (!fNode) break;

            fNode = fNode->next;
            sNode = sNode->next;

            // 若快慢指针指向相同节点
            // 则链表中有回链
            if (fNode == sNode) return true;
        }

        return false;
    }
};
