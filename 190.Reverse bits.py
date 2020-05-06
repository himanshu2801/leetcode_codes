"""
Question...
Reverse bits of a given 32 bits unsigned integer.

 

Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100
represents the unsigned integer 43261596,
so return 964176192
which its binary representation is 00111001011110000010100101000000.\
Solution...
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        x=bin(n)
        x=x.replace('0b','')
        l=32-len(x)
        if l!=0:
            x=l*"0"+x
        lst=list(x)
        d=0
        for i in range(len(lst)):
            p=2**i
            d=d+int(lst[i])*p
        return d
    
        
        
