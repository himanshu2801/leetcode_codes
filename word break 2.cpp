"""
  140. Word Break II
Hard

2973

445

Add to List

Share
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
 

Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
  """
  class Solution {
public:
    vector<string> wordBreak(string word, vector<string>& wordDict) {
    unordered_map<string,vector<string>> dp;
	if(dp.find(word)!=dp.end())
		return dp[word];
	vector<string> result;
	for(auto s:wordDict){
		if(word.substr(0,s.length())==s){
			if(word.length()==s.length()){
				result.push_back(s);
			}
			else{
				vector<string> temp=wordBreak(word.substr(s.length()),wordDict);
				for(auto x:temp)
					result.push_back(s+" "+x);
			}
		}
	}
	dp[word]=result;
	return result;
    }
};
