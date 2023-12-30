class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        counter=0
        while True:
            if num2==0 or num1==0:
                break
            if num1>num2:
                num1=num1-num2
            else:
                num2=num2-num1
            counter+=1
        return counter