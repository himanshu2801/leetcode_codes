Question...
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

"""

Solution...

class Solution:
    def isValid(self, s: str) -> bool:
        o=["(","[","{"]
        c=[")","]","}"]
        s1=[]
        top=-1
        for i in s:
            if i in o:
                s1.append(i)
                top=top+1
            elif i in c:
                pos=c.index(i)
                if ((len(s1)!=0) and (o[pos]==s1[top])):
                    s1.pop()
                    top=top-1
                else:
                    return False
        if s1==[]:
            return True
        else:
            return False
