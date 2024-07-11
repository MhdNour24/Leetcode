class Solution:
    def reverseSubString(self,firstIndex,secondIndex,OString,length):
        firstPartOfString=OString[:firstIndex-1]
        secondPartOfString=None
        if length-2==secondIndex:
            secondPartOfString=""
        else:
            secondPartOfString=OString[secondIndex+2:]
        newString=firstPartOfString+OString[firstIndex:secondIndex+1][::-1]+secondPartOfString

        return newString
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        length=len(s)
        index=0
        while index!=length:
            if s[index]=="(":
                stack.append(index)
                index+=1
            elif s[index]==")":
                prevIndex=stack.pop()
                s=self.reverseSubString(prevIndex+1,index-1,s,length)
                length-=2
                index-=1
            else:
                index+=1
        return s