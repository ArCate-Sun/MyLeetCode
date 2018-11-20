//
// Reverse Linked List
//
// Required:
// Reverse a singly linked list.
//
// Hint:
// A linked list can be reversed either iteratively or recursively.
// Could you implement both?
//


#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;

    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* reverseList(ListNode* head) {

        if (!head || !head->next) {
            return head;
        }

        auto chg_x = head;
        auto chg_y = chg_x->next;
        auto p_next = chg_y->next;
        chg_x->next = nullptr;
        while (true) {
            chg_y->next = chg_x;
            chg_x = chg_y;
            chg_y = p_next;
            if (p_next) {
                p_next = p_next->next;
            } else {
                break;
            }
        }

        return chg_x;
    }
};
