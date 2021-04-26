class Solution {
public:
    bool isSubsequence(string s, string t) {
        int first=0;
        int second=0;
        int flag=0;
        if(s==t)
            return true;
        while(first<t.length()){
            if(s[second]==t[first])
                second++;
            if(second==s.length())
            {flag=1;
            break;}
            first++;
        }
        if(flag==1)
            return true;
        else
            return false;
    }
};
