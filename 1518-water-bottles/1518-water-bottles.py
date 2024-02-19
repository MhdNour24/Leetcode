class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        counter=0
        black=numBottles
        white=0
        while True:
            counter+=black
            white+=black
            black,white=divmod(white,numExchange)
            if white<numExchange and black==0:
                break
        return counter
