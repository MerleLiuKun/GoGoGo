/*
x的平方根
by lgy 2020/10/10
*/


package mySqrt_x
/*
//顺序查找，定位平方根，此法略叼
func mySqrt_x(x int) int {
	for i :=0; i<x; i++{
		if i*i >x{
			return i-1
		}
	}
	return 
}
*/

//二分查找，定位平方根

func mySqrt_x(x int) int {
	var i int =1
	var j int =x
	for i <= j {
		mid := (i+j)/2
		if mid*mid >x {
			j = mid -1
		} else if mid *mid <x {
			i = mid +1
		} else {
			return mid
		}

	}
	return i-1
}