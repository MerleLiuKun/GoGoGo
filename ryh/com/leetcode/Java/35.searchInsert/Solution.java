//给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
class Solution {
    public int searchInsert(int[] nums, int target) {
        int len = nums.length;
        if(len == 0)
            return 0;
        else{
            for(int i=0;i<len;i++){
                if(nums[0]>target)
                    return 0;
                else if(nums[len-1]<target)
                    return len;
                else if(nums[i] == target)
                    return i;
                else if(nums[i]<target && nums[i+1] > target)
                    return i+1;
            }
        }
        return len;
    }
}