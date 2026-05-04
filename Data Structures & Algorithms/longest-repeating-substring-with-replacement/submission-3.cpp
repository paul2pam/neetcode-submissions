class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> m;
        int l = 0, r = 0;
        int maximum = 0;
        int maxf = 0;
        m[s[r]]++;
        while(r < s.size() - 1) {
            r++;
            m[s[r]]++;
            maxf = max(m[s[r]], maxf);

            if ((r - l + 1) - maxf > k) {
                m[s[l]]--;
                l++;
            }
            maximum = max(r - l + 1, maximum);
        }
        return maximum;
    }
};
