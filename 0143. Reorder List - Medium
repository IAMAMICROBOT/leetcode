/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
void reorderList(struct ListNode* head) {
    struct ListNode *slow=head;
    struct ListNode *fast=head;
    while (fast->next!=NULL && fast->next->next!=NULL) {
        slow=slow->next;
        fast=fast->next->next;
    }

    struct ListNode *prev=NULL;
    struct ListNode *curr=slow->next;
    while (curr!=NULL) {
        struct ListNode *temp=curr->next;
        curr->next=prev;
        prev=curr;
        curr=temp;
    }
    slow->next=NULL;

    struct ListNode *ptr1=head;
    struct ListNode *ptr2=prev;
    while (ptr1!=NULL && ptr2!=NULL) {
        struct ListNode *next1=ptr1->next;
        struct ListNode *next2=ptr2->next;

        ptr1->next=ptr2;
        ptr2->next=next1;

        ptr1=next1;
        ptr2=next2;
    }
}
