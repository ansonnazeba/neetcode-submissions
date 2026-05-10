class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = []
        for _ in s:
            if _.isalnum():
                new_s.append(_.lower())
        
        left = 0
        right = len(new_s) - 1

        while left <= right:
            if new_s[left] != new_s[right]:
                return False

            left += 1
            right -= 1
        
        return True

        