"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lst = []
        def findstring(current,open,close):
            if len(current)==2*n:
                if isValid(current) == True:
                    lst.append(current)
                return lst
            if open<n:
                findstring(current + '(',open+1,close)
            if close<n:
                findstring(current + ')',open,close+1)
        def isValid(s) -> bool:
            o=["("]
            c=[")"]
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
        findstring("(",1,0)
        return lst
        
