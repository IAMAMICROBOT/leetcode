/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode *prev = NULL;
    struct ListNode *temp = head;
    struct ListNode *nextn = NULL;
    
    while (temp != NULL) {
        nextn = temp->next;
        temp->next = prev;
        prev = temp;
        temp = nextn;
    }
    
    head = prev;
    return head;
    
}
