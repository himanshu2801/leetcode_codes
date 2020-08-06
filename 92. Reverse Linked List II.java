"""
Question...
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
Solution...
"""
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        ListNode Start=null;
        ListNode curr=head;
        ListNode strtm=null;
        ListNode endn=null;
        ListNode end=null;
        if (m==n){
            return head;
        }
        for (int i=1;i<=n;i++){
            if (i<m){
                Start=curr;
            }
            if (i==m){
                strtm=curr;
            }
            if (i==n){
                endn=curr;
                if(curr.next!=null){
                end=curr.next;}
                break;
            }
            curr=curr.next;
        }
        endn.next=null;
        ListNode prev=null;
        ListNode t=strtm;
        while (t!=null){
            ListNode temp=t.next;
            t.next=prev;
            prev=t;
            t=temp;
    }
        if(m!=1){
        Start.next=prev;
            strtm.next=end;
            return head;
        }
        else{
            strtm.next=end;
            return prev;
        }
    }
}
