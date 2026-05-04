class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<int> st;
        int tr = 0;

        int l = 0;
        for (int r = 0; r < s.size(); r++) {
            
            
            while (st.find(s[r]) != st.end() && l <= r) {
                st.erase(s[l]);
                l++;
            }
            tr = max(tr, r - l + 1);
            st.insert(s[r]);
        }
        
        return tr;
    }
};
