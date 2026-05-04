class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> prefix(nums.size(), 1); 
        vector<int> suffix(nums.size(), 1);
        int pre = 1, suf = 1;
        for (int i = 1; i < nums.size(); i++) {
            pre *= nums[i - 1];
            prefix[i] = pre;
        }

        for (int i = nums.size() - 2; i >= 0; i--) {
            suf *= nums[i + 1];
            suffix[i] = suf;
        }
        vector<int> product;
        for (int i = 0; i < nums.size(); i++) {
            product.push_back(prefix[i] * suffix[i]);
        }

        return product;

    }
};
