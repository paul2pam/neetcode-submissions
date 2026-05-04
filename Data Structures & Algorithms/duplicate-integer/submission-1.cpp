class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> m;
        for (int num : nums) {
            if (m[num] >= 1) return true;
            m[num]++;
        }
        return false;
    }
};

/*
*/