class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s(nums.begin(), nums.end());
        int to_return = 0;

        for (int n : s) {
            if (!s.count(n - 1)) {
                int i = 0;
                while (s.count(n + i)) {
                    i++;
                }
                to_return = max(i, to_return);
            }
        }
        return to_return;
    }
};
