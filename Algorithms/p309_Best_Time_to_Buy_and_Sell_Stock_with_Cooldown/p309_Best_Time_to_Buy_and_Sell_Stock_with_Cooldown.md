Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]

Solution:
three possible states on each day:
s0: not holding
s1: holding
s2: just sold

sj[i]=max profit on day i with state sj

s0[i]=
max(s0[i-1],s2[i-1]), i>=3
s0[1], i=2
0, i=1

s1[i]=
max(s0[i-1]-prices[i],s1[i-1]), i>=2
-price1, i=1

s2[i]=
s1[i-1]+prices[i], i>=2
meaningless (or minus infinity for simplicity), i=1


+--+--+--+--+
|d1|d2|d3|d4|
+--+--+--+--+
|s0|s0|s0|s0|
|s1|s1|s1|s1|
|  |s2|s2|s2|
+--+--+--+--+