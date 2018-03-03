//
// Best Time to Buy and Sell Stock II
//
// 要求:
// 假设有一个数组，它的第 i 个元素是一个给定的股票在第 i 天的价格。
// 设计一个算法来找到最大的利润。你可以完成尽可能多的交易（多次买卖股票）。然而，你不能同时参与多个交易（你必须在再次购买前出售股票）。
//

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {

        // 判断 nums 为空
        if (prices.empty()) {
            return 0;
        }

        int min = prices[0];
        int max = 0;

        int isBought = false;
        int price_when_bought = 0;
        int sum = 0;

        for (int i = 0; i < prices.size() - 1; ++i) {
            if (!isBought) {
                if (min > prices[i + 1]) {
                    min = prices[i + 1];
                } else if (min < prices[i + 1]) {
                    cout << "buy: " << min << endl;
                    isBought = true;
                    max = prices[i + 1];
                    price_when_bought = min;
                }
            } else {
                if (max < prices[i + 1]) {
                    max = prices[i + 1];
                } else if (max > prices[i + 1]) {
                    cout << "sell: " << max << endl;
                    isBought = false;
                    min = prices[i + 1];
                    sum = sum + max - price_when_bought;
                }
            }
        }
        if (isBought) {
            cout << "sell: " << max << endl;
            sum = sum + max - price_when_bought;
        }

        return sum;
    }
};

