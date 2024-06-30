class Solution:
    def trailingZeroes(self, n: int) -> int:
        counter=0
        power=1
        while True:
            number=5**power
            if number>n:
                break
            counter+=n//number
            power+=1
        return counter