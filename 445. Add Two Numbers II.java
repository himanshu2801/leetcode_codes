"""
Question...
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
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
import java.lang.Math;
class Solution {
    static ListNode reverse(ListNode head){
        ListNode prev=null;
        while (head!=null){
            ListNode temp=head.next;
            head.next=prev;
            prev=head;
            head=temp;
        }
        return prev;}
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode temp = new ListNode(0), newlist = temp;
        l1=reverse(l1);
        l2=reverse(l2);
        int carry=0;
        while(l1!=null || l2!=null){
            int sum=carry;
            if(l1!=null){
                sum=sum+l1.val;
                l1=l1.next;
            }
            if(l2!=null){
                sum=sum+l2.val;
                l2=l2.next;
            }
             newlist.next = new ListNode(sum % 10);
            carry = sum / 10;
            newlist = newlist.next;
        }
         if(carry != 0){
            newlist.next = new ListNode(carry);
            newlist = newlist.next;
        }
        temp=reverse(temp.next);
        return temp;
        }
}
