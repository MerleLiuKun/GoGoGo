from turtle import st


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        key_map = {")": "(", "}": "{", "]": "["}
        for ss in s:
            if not stack:
                stack.append(ss)
            else:
                if ss in key_map and stack[-1] == key_map[ss]:
                    stack.pop()
                else:
                    stack.append(ss)
        
        return not stack
    
    def isValid2(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        key_map = {")": "(", "}": "{", "]": "["}
        for ch in s:
            if ch in key_map:
                if stack and stack[-1] == key_map[ch]:
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
        return not stack
    
    def isValid3(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        key_map = {")": "(", "}": "{", "]": "["}
        for ch in s:
            if ch in key_map:
                # 如果 出现右边 但是没有左边 或者栈顶的不是当前对应的左边 则说明 该右边无匹配 直接报错
                if not stack or stack[-1] != key_map[ch]:
                    return False
                # 匹配上了 就弹出当前的栈顶
                stack.pop()
            else:
                stack.append(ch)
        return not stack

if __name__ == "__main__":
    s = Solution()
    print(s.isValid("([)]"))
    print(s.isValid2("([}}])"))

