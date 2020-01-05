package letcode.solution;

/**
 * @author lichong<br />
 * @Description: 两数之和<br />
 * @date 2020/1/5  21:31<br/>
 */
public class TwoSum {
    /**
        两遍哈希表法
        通过以空间换取速度的方式，我们可以将查找时间从 O(n)O(n) 降低到 O(1)O(1)。哈希表正是为此目的而构建的，它支持以 近似 恒定的时间进行快速查找。我用“近似”来描述，是因为一旦出现冲突，查找用时可能会退化到 O(n)O(n)。但只要你仔细地挑选哈希函数，在哈希表中进行查找的用时应当被摊销为 O(1)O(1)。

        一个简单的实现使用了两次迭代。在第一次迭代中，我们将每个元素的值和它的索引添加到表中。然后，在第二次迭代中，我们将检查每个元素所对应的目标元素（target - nums[i]target−nums[i]）是否存在于表中。注意，该目标元素不能是 nums[i]nums[i] 本身！
    */
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
                    for (int i = 0; i < nums.length; i++) {
                        map.put(nums[i], i);
                    }
                    for (int i = 0; i < nums.length; i++) {
                        int complement = target - nums[i];
                        if (map.containsKey(complement) && map.get(complement) != i) {
                            return new int[] { i, map.get(complement) };
                        }
                    }
                    throw new IllegalArgumentException("No two sum solution");
    }
}
