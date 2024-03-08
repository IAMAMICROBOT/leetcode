/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    int c=0;
    struct ListNode *temp;
    temp=head;
    while(temp){
        c++;
        temp=temp->next;
    }
    int p=c-n;
    if (p<0 || n<=0) {
        return head;
    }
    if (p==0) {
        struct ListNode *newHead = head->next;
        free(head);
        return newHead;
    }
    temp=head;
    struct ListNode *prev;
    for(int i=0;i<p;i++){
        prev=temp;
        temp=temp->next;
    }
    prev->next=temp->next;
    free(temp);
    return head;
    
}
