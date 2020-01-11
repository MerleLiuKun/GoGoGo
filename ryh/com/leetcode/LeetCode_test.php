<?php
//9：回文数
function isPalindrome($x) {
    if($x<0){
        return false;
    }
    if ($x == 0){
        return true;
    }
    $result = 0;
    $y = $x;
    while($y!=0){
        $p = $y%10;
        $y = intval($y/10);
        $result = $result * 10 + $p;
    }
    if( $x==$result){
        return true;
    }
    else {
        return false;
    }
}
//13：罗马字母转数字
function romanToInt($s) {
    $arr = array(
        'I'=>1,
        'V'=>5,
        'X'=>10,
        'L'=>50,
        'C'=>100,
        'D'=>500,
        'M'=>1000,
    );
    $tmp[] = str_split($s);
    $result = 0;
    for($i=0; $i<count($tmp[0]);$i++)
    {
        if($i>=1 && $arr[$tmp[0][$i]]>$arr[$tmp[0][$i-1]])
        {
            $result += $arr[$tmp[0][$i]]-2*$arr[$tmp[0][$i-1]];
        }
        else
        {
            $result += $arr[$tmp[0][$i]];
        }
    }
    return $result;
}
//14：最长公共前缀
function longestCommonPrefix($strs)
{
    if(count($strs)==1)
        return $strs[0];
    if(count($strs)==0)
        return "";
    $prefix = $strs[0];
    for($i=0;$i<count($strs);$i++)
    {
        $str = "";
        for($j=0;$j<min(strlen($prefix),strlen($strs[$i]));$j++)
        {
            if($prefix[$j] == $strs[$i][$j])
                $str.= $strs[$i][$j];
            else
                break;
        }
        $prefix = $str;
        if(empty($prefix))
        {
            break;
        }
    }
    return $prefix;
}
//判断是否是有效的括号
function isValid($s) {
    $arr = array();
    for($i=0;$i<strlen($s);$i++)
    {
        if($s[$i] == '(' || $s[$i] == '[' || $s[$i] == '{'){
            $arr[$i] = $s[$i];
        }
        else{
            if(count($arr) == 0){
                return false;
            }
            if($arr[count($arr)-1] == '(' && $s[$i] !=')')
            {
                return false;
            }
            if($arr[count($arr)-1] == '[' && $s[$i] !=']')
            {
                return false;
            }
            if($arr[count($arr)-1] == '{' && $s[$i] !='}')
            {
                return false;
            }
            unset($arr[count($arr)-1]);
        }
    }
    if(empty($arr))
    {
        return true;
    }
}
