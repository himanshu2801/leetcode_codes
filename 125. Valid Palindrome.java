"""
  Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
  """
  class Solution {
    public boolean isPalindrome(String s) {
        String n="";
        
        for(int i=0;i<s.length();i++){
            if(Character.isUpperCase(s.charAt(i))||Character.isLowerCase(s.charAt(i)))
                n+=s.charAt(i);
            if(s.charAt(i)>=48 && s.charAt(i)<=57)
                n+=s.charAt(i);
        }
        n=n.toLowerCase();
        int left=0;
        int right=n.length()-1;
        while(left<n.length()/2){
            if(n.charAt(left)!=n.charAt(right))
                return false;
            left++;
            right--;
        }
        return true;
    }
}
