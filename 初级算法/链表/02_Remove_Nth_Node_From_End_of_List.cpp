//
// Remove Nth Node From End of List
//
// 要求:
// 给定一个链表，删除链表的倒数第 n 个节点并返回头结点。
//
// 例如:
// 给定一个链表: 1->2->3->4->5, 并且 n = 2.
// 当删除了倒数第二个节点后链表变成了 1->2->3->5.
//
// 说明:
// 给的 n 始终是有效的。
// 尝试一次遍历实现。
//

#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;

    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    void deleteNextNode(ListNode *node) {
        auto next = node->next;
        node->next = next->next;
        delete next;
    }

    ListNode *removeNthFromEnd(ListNode *head, int n) {

        auto front = head;
        for (int i = 0; i < n + 1; ++i) {
            auto new_node = new ListNode(0);
            new_node->next = front;
            front = new_node;
        }

        auto rear = head;
        while (rear) {
            rear = rear->next;
            front = front->next;
        }

        if (front ->next == head) {
            this->deleteNextNode(front);
            return front->next;
        } else {
            this->deleteNextNode(front);
            return head;
        }
    }
};
