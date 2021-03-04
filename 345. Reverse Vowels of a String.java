"""
  Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
  """
  class Solution {
    public String reverseVowels(String s) {
       Set<Character> vowels = new HashSet<>();
        vowels.add('a');vowels.add('u');vowels.add('o');vowels.add('i');vowels.add('e');
        vowels.add('A');vowels.add('U');vowels.add('O');vowels.add('I');vowels.add('E');
        int left=0;
        int right=s.length()-1;
        char []ch=s.toCharArray();
        while(left<right){
            if(vowels.contains(ch[left])&&vowels.contains(ch[right])){
                char temp=ch[left];
                ch[left]=ch[right];
                ch[right]=temp;
                left++;
                right--;
            }
            else if(!vowels.contains(ch[left])&&vowels.contains(ch[right]))
                left++;
            else if(vowels.contains(ch[left])&&!vowels.contains(ch[right]))
                right--;
            else
            {left++;
            right--;}
        }
        String output="";
        for(int i=0;i<ch.length;i++)
            output+=ch[i];
        return output;
    }
}
