/*
买卖股票的最佳时机
by lgy 2020/1/10
*/
package maxProfit
//遍历所有获利
func maxProfit(price []int)int {
	max :=0
	for i :=0; i<len(price)-1; i++{
		for j :=i+1; j<len(price); j++{
			delta := price[j] - price[i]
			if delta > max {
				max = delta

			}
		}
	}
	return max
}

