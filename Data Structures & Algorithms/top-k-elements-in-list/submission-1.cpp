class Solution {
public:
    static bool comparePairs(pair<int, int> a, pair<int, int> b) {
        return a.second > b.second;
    }
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> m;
        for (int num : nums) {
            m[num]++;
        }

        vector<pair<int, int>> items(m.begin(), m.end());
        sort(items.begin(), items.end(), comparePairs);

        vector<int> to_return;
        for (int i = 0; i < k; i++) {
            to_return.push_back(items[i].first);
        }
        return to_return;
    }
};
