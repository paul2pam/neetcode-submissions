class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<string> copy = strs;
        vector<vector<string>> to_return;
        unordered_map<string, vector<int>> m;
        for (int i = 0; i < copy.size(); i++) {
            sort(copy[i].begin(), copy[i].end());
            m[copy[i]].push_back(i);
        }
        for (auto& [k, v] : m) {
            vector<string> to_add;
            for (int i : v) {
                to_add.push_back(strs[i]);
            }
            to_return.push_back(to_add);
        }
        return to_return;
    }
};
