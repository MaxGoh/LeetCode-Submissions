class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = 0

        for i in range(len(s) - 1):

            if symbol_values[s[i]] < symbol_values[s[i + 1]]:
                result -= symbol_values[s[i]]
            else:
                result += symbol_values[s[i]]

        result += symbol_values[s[-1]]

        return result
