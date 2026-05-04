class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> m;
        for(char c : s) {
            m[c]++;
        }
        for (char c : t) {
            m[c]--;
        }
        for (const auto& kv : m) {
            if (kv.second != 0) return false;
        }
        return true;
    }
};
