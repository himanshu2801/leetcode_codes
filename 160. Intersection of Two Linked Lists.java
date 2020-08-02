"""
Question...
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.

 

Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). 
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. 
There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
Solution...
"""
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        Set<ListNode> h=new HashSet<>();
        ListNode t1=headA;
        while(t1!=null){
            h.add(t1);
            System.out.println(t1);
            t1=t1.next;
        }
        if (h.isEmpty()){
            return null;
        }
        ListNode t2=headB;
        while(t2!=null){
            if(h.contains(t2)){
                return t2;
            }
            else{
                t2=t2.next;
            }
        }
        return null;
        
    }
}
