class Solution {
public:
    int sumOfUnique(vector<int>& nums) {
        unordered_map<int,int> mp;
        for(auto x:nums)
        {
            if(mp[x]==0)
                mp[x]=1;
            else
                mp[x]++;
        }
        int sum=0;
        for(auto x:nums){
            if(mp[x]==1)
                sum+=x;
        }
        return sum;
    }
};
