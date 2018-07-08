class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        minStr = ""
        shortestStr = min(strs, key=len)
        tempCount = 0

        for i in range(0, len(shortestStr)):
            for j in range(0, len(strs)):
                if strs[j][i] == shortestStr[i]:
                    tempCount += 1
            if (tempCount == len(strs)):
                minStr += (shortestStr[i])
                tempCount = 0
            else:
                break

        return minStr
