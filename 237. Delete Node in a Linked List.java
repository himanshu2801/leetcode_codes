"""
question...
Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list.Input: head = [4,5,1,9], n = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.Input: head = [4,5,1,9], n = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
Example 3:

Input: head = [1,2,3,4], n = 3
Output: [1,2,4]
Example 4:

Input: head = [0,1], n = 0
Output: [1]
Example 5:

Input: head = [-3,5,-99], n = -3
Output: [5,-99]

Constraints:

The number of the nodes in the given list is in the range [2, 1000].
-1000 <= Node.val <= 1000
The value of each node in the list is unique.
The node given to be deleted exists in the list, and cannot be the tail value.
Solution...
"""
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void deleteNode(ListNode node) {
        boolean flag=true;
        while(flag==true){
            if (node.next.next!=null){
                node.val=node.next.val;
                node=node.next;
            }
            else{
                node.val=node.next.val;
                node.next=null;
                flag=false;
            }
        }
        
    }
}
