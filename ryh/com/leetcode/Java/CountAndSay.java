package com.string;

public class CountAndSay {
    public static void main(String[] args) {
        String str = countAndSay(5);
    }
    public static String countAndSay(int n) {
        // 递归终止条件
        if (n == 1) {
            return "1";
        }
        StringBuffer res = new StringBuffer();
        // 拿到上一层的字符串
        System.out.println("n1:"+n);
        String str = countAndSay(n - 1);
        System.out.println("n2:"+n);
        System.out.println("str:"+str);
        int length = str.length();
//        System.out.println(" length:"+length);
        // 开始指针为0
        int start = 0;
        // 注意这从起始条件要和下面长度统一
        for (int i = 1; i < length + 1; i++) {
            // 字符串最后一位直接拼接
            if (i == length) {
                res.append(i - start).append(str.charAt(start));
                // 直到start位的字符串和i位的字符串不同，拼接并更新start位
            } else if (str.charAt(i) != str.charAt(start) ) {
                res.append(i - start).append(str.charAt(start));
                start = i;
            }
        }
        return res.toString();
    }

}
