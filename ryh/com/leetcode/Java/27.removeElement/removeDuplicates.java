package com.leetcode;
import java.util.Arrays;
public class  removeElement{
    //移除元素：去掉nums中的val值
    public int removeElement(int[] nums, int val) {
        int i=0;
        for(int j=0;j<nums.length;j++)
        {
            if(nums[j] != val)
            {
                nums[i] = nums[j];
                i++;
            }
        }
        System.out.println(Arrays.toString(nums));
        return i;
    }
}
