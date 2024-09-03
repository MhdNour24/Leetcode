class Solution:
    def stringToInteger(self,string):
        newString=""
        for i in string:
            newString+=str(ord(i)-96)
        return int(newString)
    def sumOfDigits(self,number):
        top=0
        while number!=0:
            lastDigit=number%10
            top+=lastDigit
            number=number-lastDigit
            number=number//10
        return top
    def getLucky(self, s: str, k: int) -> int:
        number=self.stringToInteger(s)
        for i in range(k):
            number=self.sumOfDigits(number)
        return number

