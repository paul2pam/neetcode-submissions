class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::map<int, int> m;
        for (int num : nums) {
            if (m[num] >= 1) return true;
            m[num]++;
        }
        return false;
    }
};

/*
*/