class Solution:
    def isValid(self, s) :
        if len(s)%2!=0:
            return False
        
        stack = list()

        dic = {'(':')','{':'}','[':']'}
        
        for i, c in enumerate(s):
            if s[i] in dic:
                stack.append(s[i])
            else:
                if len(stack)!=0 and dic[stack[-1]] == s[i]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True
        