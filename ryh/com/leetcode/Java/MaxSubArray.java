package com.leetcode;

import java.lang.reflect.Array;
import java.util.Arrays;

/*
53、最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6
* */
public class MaxSubArray {
    public static void main(String[] args) {
        int[] nums = {-2, 1};
        System.out.println(Arrays.toString(nums));
        MaxSubArray maxSubArray = new MaxSubArray();
        System.out.println(maxSubArray.maxSubArray(nums));
    }

    public int maxSubArray(int[] nums) {
        int maxResult = nums[0];
        for (int i = 0; i < nums.length; i++) {
            int sum = 0;

            for (int j = i; j < nums.length; j++) {
                sum += nums[j];//前n项连续数之和
                maxResult = Math.max(maxResult, sum);
            }
            System.out.println("最大值是:" + maxResult);
        }
        return maxResult;
    }
}
