class Solution {
public:
    int findMin(vector<int> &nums) {
        int l = 0, r = nums.size() - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] < nums[r]) { //if right part is sorted
                r = mid;
            } else { //if left part is sorted
                l = mid + 1;
            }
        }
        return nums[r];
    }
};
