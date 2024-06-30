class Solution:
    def countDigits(self, num: int) -> int:
        counter=0
        number=num
        while number:
            lastNumber=number%10
            if num%lastNumber==0:
                counter+=1
            number=number//10
        return counter
            