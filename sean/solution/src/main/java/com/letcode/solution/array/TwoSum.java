package com.letcode.solution.array;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * @author lichong<br />
 * @Description: 两数之和<br />
 * @date 2020/1/6  15:27<br/>
 */
public class TwoSum {
    public static void main(String[] args) {
        int[] nums = new int[]{5, 7, 8, 10, 14, 9};
        int[] result = twoSum(nums, 14);
        System.out.println(Arrays.toString(result));
        int[] result2 = twoSum2(nums, 14);
        System.out.println(Arrays.toString(result2));
    }

    /**
     * 两遍哈希表
     * @param nums
     * @param target
     * @return
     */
    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement) && map.get(complement) != i) {
                return new int[]{i, map.get(complement)};
            }
        }
        throw new IllegalArgumentException("No two sum solution");
    }

    /**
     * 一遍哈希表
     * @param nums
     * @param target
     * @return
     */
    public static int[] twoSum2(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i };
            }
            map.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}
