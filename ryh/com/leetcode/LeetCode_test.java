package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;
public class LeetCode_test {
	//7：反转整数
	int reverse(int x){
		int rev = 0;
		while(x!=0){
			int pop = x % 10;
			x/=10;
			if(rev > Integer.MAX_VALUE/10 || (rev == Integer.MAX_VALUE/10 && pop>7))
			{
				return 0;
			}
			if(rev <Integer.MIN_VALUE/10 ||(rev == Integer.MIN_VALUE/10 && pop<-8))
			{
				return 0;
			}
			rev = rev*10+pop;
		}
		return rev;
	}
	//判断是否是回文数
	boolean isPalindrome(int x){
		if(x==0){
			return true;
		}
		else if(x < 0){
			return false;
		}
		else{
			int result = 0;

			int y = x;

			while(y!=0){
				int p = y%10;
				y = y/10;

				result = result * 10 + p;
			}
			return result==x;
		}
	}
	//罗马文字转数字
	int romanToInt(String s)
	{
		Map<Character,Integer> map = new HashMap();
		map.put('I',1);
		map.put('V',5);
		map.put('X',10);
		map.put('L',50);
		map.put('C',100);
		map.put('D',500);
		map.put('M',1000);

		int result = 0;
		for(int i=0;i<s.length();i++)
		{
			//
			if(i>=1 && map.get(s.charAt(i))>map.get(s.charAt(i-1)))
			{
				result += map.get(s.charAt(i))- 2*map.get(s.charAt(i-1));
			}
			else
			{
				result += map.get(s.charAt(i));
			}
		}
		return result;
	}
	//最长公共前缀
	public String longestCommonPreix(String [] strs) {

		if (strs.length == 0) {
			return "";
		}
		String prefix = strs[0];
		for (int i = 1; i < strs.length; i++) {
			while(strs[i].indexOf(prefix)!=0){
				prefix = prefix.substring(0,prefix.length()-1);
			}
			if(prefix.isEmpty()){
				return "";
			}
		}
		return prefix;
	}
	//是否是有效的括号
	boolean isValid(String s) {
		Deque<Character> stack = new ArrayDeque<>();
		for(int i=0;i<s.length();i++)
		{
			if(s.charAt(i) == '{' || s.charAt(i) == '[' || s.charAt(i) == '(')
			{
				stack.push(s.charAt(i));
			}
			else
			{
				if(stack.isEmpty())
					return false;
				else
				{
					if(stack.peek()=='(' && s.charAt(i)!=')')
						return false;
					else if(stack.peek()=='[' && s.charAt(i)!=']')
						return false;
					else if(stack.peek()=='{' && s.charAt(i)!='}')
						return false;
					stack.pop();
				}
			}
		}
		return stack.isEmpty();
	}
}
