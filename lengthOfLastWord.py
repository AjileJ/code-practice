class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for item in s:
            count += 1
            if item == ' ':
                count = 0
        return count