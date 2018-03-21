//
// Remove Nth Node From End of List
//
// Required:
// Given a linked list, remove the nth node from the end of list and return its head.
//
// Example:
// Given linked list: 1->2->3->4->5, and n = 2.
// After removing the second node from the end, the linked list becomes 1->2->3->5.
//
// Note:
// Given n will always be valid.
// Try to do this in one pass.
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
