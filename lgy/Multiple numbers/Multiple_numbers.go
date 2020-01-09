/*
排序后取 sortHash[n/2] O(nlogn)
by lgy
2020/1/9

*/


package main 
import (
	"sort"
	"fmt"
)

func majorityElement(nums []int) int {
    sort.Ints(nums)
    return nums[len(nums)/2]
}
func main(){
	fmt.Println();
}
