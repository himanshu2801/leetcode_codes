"""
Question...
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly
Solution...
"""
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num,num0=0,0
        for i in range(len(num1)):
            x = ord(num1[i]) - ord('0')
            num= num + x*(10**(len(num1)-i-1))
        for i in range(len(num2)):
            x=ord(num2[i])-ord('0')
            num0=num0+x*(10**(len(num2)-i-1))
        return str(num+num0)
            
            
        
