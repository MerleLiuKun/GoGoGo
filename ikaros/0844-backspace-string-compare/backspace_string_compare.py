class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = self.backspace(s)
        t_stack = self.backspace(t)

        return s_stack == t_stack
    
    def backspace(self, s: str) -> list:
        stack = []
        for ch in s:
            if ch == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return stack
    
    def backspaceCompare2(self, s, t: str) -> bool:
        i, j = len(s) - 1, len(t) -1
        skip_s = skip_t = 0

        while i>=0 or j>=0:
            while i >= 0:
                if s[i] == "#":
                    skip_s += 1
                    i -= 1
                elif skip_s >0:
                    skip_s -=1
                    i -= 1
                else:
                    break
            while j>=0:
                if t[j] == "#":
                    skip_t += 1
                    j -= 1
                elif skip_t > 0:
                    skip_t -=1 
                    j -= 1
                else:
                    break
            
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i>=0 or j>=0:
                return False
            
            i -= 1
            j -= 1
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.backspaceCompare2("ab#c", "ad#c"))
    print(s.backspaceCompare2("ab##", "c#d#"))
    print(s.backspaceCompare2("a#c", "b"))
    print(s.backspaceCompare2("y#fo##f", "y#f#o##f"))

