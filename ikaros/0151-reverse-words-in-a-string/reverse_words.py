class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.strip().split()
        return " ".join([word for word in arr[::-1]])
    

    


if __name__ == "__main__":
    ms = "a good   example"
    print(Solution().reverseWords(ms))