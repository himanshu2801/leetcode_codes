"""
Question...
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
Example 1:

Input:
26

Output:
"1a"
Example 2:

Input:
-1

Output:
"ffffffff"
Solution...
"""
class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return "0"
        s=""
        lst=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        if num<0:
            num=num+2**32  //that will convert signed integer into unsigned. however you can skip the 2's compliment method 
                           //by using this
        while num!=0:
            temp=num%16
            s=s+lst[temp]
            num=num//16
        return s[::-1]
            
        
