"""
  Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.

 

Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
Example 2:

Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]
Example 3:

Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]
Example 4:

Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]
Example 5:


Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]
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
    List<Integer> list=new ArrayList<Integer>();
    private void getSingleList1(TreeNode node){
        list.add(node.val);
        if(node==null)
            return ;
        if(node.left!=null)
            getSingleList1(node.left);
        if(node.right!=null)
            getSingleList1(node.right);
    }
    private void getSingleList2(TreeNode node){
        list.add(node.val);
        if(node==null)
            return ;
        if(node.left!=null)
            getSingleList2(node.left);
        if(node.right!=null)
            getSingleList2(node.right);
    }
    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
        if(root1==null && root2==null)
            return list;
        else if(root1!=null&&root2==null)
            getSingleList1(root1);
        else if(root2!=null&&root1==null)
            getSingleList2(root2);
        else{
            getSingleList1(root1);
        getSingleList2(root2);}
        Collections.sort(list);
        return list;
    }
}
