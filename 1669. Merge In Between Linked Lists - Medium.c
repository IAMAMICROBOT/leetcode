/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeInBetween(struct ListNode* list1, int a, int b, struct ListNode* list2) {
    struct ListNode *ptr1 = list1, *ptr2 = list2;
    while (b--) 
        ptr1=ptr1->next;
    while (ptr2->next) 
        ptr2 = ptr2->next;
    ptr2->next = ptr1->next;
    a--;
    ptr1 = list1;
    while (a--) 
        ptr1 = ptr1->next;
    ptr1->next = list2;
    return list1;
}
