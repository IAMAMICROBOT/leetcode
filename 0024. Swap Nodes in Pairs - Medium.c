/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head) {
    struct ListNode *ptr=head;
    int temp;
    while(ptr && ptr->next){
        temp=ptr->val;
        ptr->val=ptr->next->val;
        ptr->next->val=temp;
        ptr=ptr->next->next;
    }
    return head;
}
