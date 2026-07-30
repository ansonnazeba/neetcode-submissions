/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (list1 == nullptr && list2 == nullptr)
            return nullptr;
        else if (list1 == nullptr)
            return list2;
        else if (list2 == nullptr)
            return list1;

        struct ListNode dummy;
        dummy.next = nullptr;
        struct ListNode* dummyPtr = &dummy;
        struct ListNode* curr1 = list1;
        struct ListNode* curr2 = list2;

        while (curr1 && curr2) {
            if (curr1->val <= curr2->val) {
                dummyPtr->next = curr1;
                curr1 = curr1->next;

            } else {
                dummyPtr->next = curr2;
                curr2 = curr2->next;
            }
            dummyPtr = dummyPtr->next;
        }

        while (curr1) {
            dummyPtr->next = curr1;
            curr1 = curr1->next;
            dummyPtr = dummyPtr->next;
        }

        while (curr2) {
            dummyPtr->next = curr2;
            curr2 = curr2->next;
            dummyPtr = dummyPtr->next;           
        }

        return dummy.next;
    }
};
