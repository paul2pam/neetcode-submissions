class Solution {
public:
    int maxArea(vector<int>& heights) {
        int maximum = 0;
        int left = 0;
        int right = heights.size() - 1;

        while (left < right) {
            int area = min(heights[left], heights[right]) * (right - left);
            maximum = max(area, maximum);
            if (heights[left] < heights[right]) {
                left++;
            } else right--;
        }
        return maximum;
    }
};
