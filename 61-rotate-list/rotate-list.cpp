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
    ListNode* rotateRight(ListNode* head, int k) {
        if(k==0){
            return head;
        }
        if(head==NULL){
            return head;
        }
        int totallength=0;
        ListNode* temp=head;
        while(temp){
            totallength+=1;
            temp=temp->next;
        }
        if(k>totallength){
            k=k%totallength;
        }
        if(k==totallength){
            return head;
        }
        if(k==0){
            return head;
        }
        int m= totallength-k;
        ListNode* ans = head;
        ListNode* tmp = ans;
        int chk=1;
        while(chk<m){
            chk+=1;
            ans=ans->next;
        }
        ListNode* hmp = ans->next;
        // cout<<ans->val;
        ans->next=NULL;
        ListNode* gmp=hmp;
        while(hmp->next){
            hmp=hmp->next;
        }
        hmp->next=tmp;
        return gmp;


    }
};