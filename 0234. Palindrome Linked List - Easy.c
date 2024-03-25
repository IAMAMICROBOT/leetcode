/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool isPalindrome(struct ListNode* head) {
    struct ListNode *temp=head;
    int c=0;
    while(temp){
        c++;
        temp=temp->next;
    }
    int ar[c];
    for(int i=0;i<c;i++){
        ar[i]=head->val;
        head=head->next;
    }
    int left=0,right=--c;
    while(left<right){
        if(ar[left]!=ar[right])
            return false;
        left++;
        right--;
    }
    return true;
}
