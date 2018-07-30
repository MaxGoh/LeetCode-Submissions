class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if needle == "":
            return 0

        continueCheck = False
        currentCheck = ""
        index = 0

        for i in len(haystack):
            for j in len(needle):
                if continueCheck = True:

                else:
                    if (haystack[i] == needle[j]):
                        continueCheck = True
                        index = i
                    else:
                        continueCheck = False
