<?php
/*暴力破解，两个数相加判断是否等于目标值
复杂度较高
 * */
function twoSum($nums, $target) {
    for($i=0;$i<count($nums)-1;$i++){
        for($j=$i+1;$j<count($nums);$j++){
            if($nums[$i]+$nums[$j]==$target){
                $result  = array($i,$j);
                return $result;
            }
        }
    }
    return false;
}
$nums = array(2,5,6,4);
$target = 7;
print_r(twoSum($nums,$target));