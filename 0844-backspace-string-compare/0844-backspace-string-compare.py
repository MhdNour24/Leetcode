class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        str1 ,str2 = [], []
        for i in s:
            if i == '#':
                if str1:
                    str1.pop()
            else:
                str1.append(i)
        for i in t:
            if i == '#':
                if str2:
                    str2.pop()
            else:
                str2.append(i)
        return str1 == str2
        