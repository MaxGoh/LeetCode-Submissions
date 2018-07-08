class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True

        tempStack = []

        for i in range(0, len(s)):

            if not tempStack:
                tempStack.append(s[i])

            else:
                if s[i] == '(' or s[i] == '{' or s[i] == '[':
                    tempStack.append(s[i])

                else:
                    c = tempStack.pop()
                    if self.reverseParam(c) != s[i]:
                        return False

        if not tempStack:
            return True

        return False

    def reverseParam(self, c):
        if c == '{':
            return '}'
        elif c == '(':
            return ')'
        elif c == '[':
            return ']'
        else:
            return 'invalid'
