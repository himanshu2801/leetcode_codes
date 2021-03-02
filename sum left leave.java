"""
  Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24
      """
  /**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int sum=0;
    private void getsum(TreeNode node,boolean is_Left){
        if(is_Left==true && node.left==null &&node.right==null){
        sum+=node.val;
            return;
        }
        if(node.left!=null)
            getsum(node.left,true);
         if(node.right!=null)
             getsum(node.right,false);
    }
    public int sumOfLeftLeaves(TreeNode root) {
        if(root==null)
            return 0;
        getsum(root,false);
        return sum;
    }
}
