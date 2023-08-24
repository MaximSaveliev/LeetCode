class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        x_revers = x[::-1]
        if x == x_revers:
            return True
        else:
            return False