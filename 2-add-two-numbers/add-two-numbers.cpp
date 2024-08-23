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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
       ListNode* a=l1;
       ListNode* pre=l1;
       int i=0;
       while(a!=NULL)//length of linked list1
       {
           i++;
           a=a->next;
       }
       ListNode* h=l2;
       ListNode* no=l2;
       int j=0;
       while(h!=NULL)//length of linked list2
       {
           j++;
           h=h->next;
       }
       ListNode* pree=pre;
       ListNode* noo=no;
       if(i!=j){//length equal kakapothey
       while(pre->next!=NULL)//linked list1 ending varaku traverse chesthunna 
       {
           pre=pre->next;
       }
       while(no->next!=NULL)//linked list2 ending varaku traverse chesthunna
       {
           no=no->next;
       }
       }
       if(j>i)//a list lakkuva untey a list ending loo "0" add chesthunna 
       {      //because adding lo two list same length undali kabatti
           int ha=j-i;
           int k=0;
           while(k<ha)
           {
               ListNode* att=new ListNode(0);
               pre->next=att;
               pre=pre->next;
               k++;
           }
       }
       else if(j<i)
       {
           int hi=i-j;
           int kk=0;
           while(kk<hi)
           {
               ListNode* al=new ListNode(0);
               no->next=al;
               no=no->next;
               kk++;
           }
       }  
       int carry=0;
       ListNode* fil=new ListNode(0);//kotha list loki sum append chesthunnam
       ListNode* fina=fil;
       while(pree!=NULL && noo!=NULL)
       {
           int saa=carry+pree->val+noo->val;//8+7=15 so sum chesthunte inko value extra vasthundu so,carry add chestha next value ki velthadi
           if(saa>9)
           {
               carry=saa/10;
               saa=saa%10;
           }
           else
           {
               carry=0;
           }
           ListNode* help=new ListNode(saa);
           fil->next=help;
           fil=fil->next;
           pree=pree->next;
           noo=noo->next;
       }
       if(carry!=0)//oka vela list end ipoindhi but carry undi pothey 78+25=103 "1" value extra
       {
           ListNode* hello=new ListNode(carry);
           fil->next=hello;
       }
       return fina->next; 
    }
};