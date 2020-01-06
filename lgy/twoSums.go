/*
The sum of two nums
by lgy 1/6
*/
package main 
import "fmt"
//暴力破解法
func twoSum(nums []int, target int) []int {
	var re []int
	for i:=0; i < len(nums)-1;i++{
		for j:= i + 1; j < len(nums); j++{
			if nums[i] +nums[j] == target{
				re = []int{i, j}
				break
			}
		}
	}
    return re
}
func main(){
	fmt.Println("done")
}