//
// Best Time to Buy and Sell Stock II
//
// Required:
// Say you have an array for which the ith element is the price of a given stock on day i.
// Design an algorithm to find the maximum profit.
// You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times).
// However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
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

