class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy = prices[0];
        int profit = 0;
        int i = 1;
        while (i < prices.size()) {
            int sell = prices[i];
            if (sell < buy) buy = sell;
            profit = max(profit, sell - buy);
            i++;
        }
        return profit;
    }
};
