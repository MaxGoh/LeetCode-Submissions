from math import floor

class Solution:
    def reverseInt(self, num):
        """
        :type num: int
        :rtype: int
        """
        reverseNum = 0

        while (num > 0):
            reverseNum = (reverseNum * 10) + num % 10
            num = floor(num / 10)

        return reverseNum

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        if self.reverseInt(x) == x:
            return True

        return False
