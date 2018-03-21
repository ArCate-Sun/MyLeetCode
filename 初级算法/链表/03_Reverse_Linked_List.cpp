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

int main() {

    Solution solution;

    auto *head = new ListNode(1);
    auto node = head;
    for (int i = 0; i < 5; ++i) {
        node = node->next = new ListNode(i);
    }

    auto rs = solution.reverseList(head);

    for (auto n = rs; n; n = n->next) {
        cout << n->val << " ";
    }
    cout << endl;

    return 0;
}