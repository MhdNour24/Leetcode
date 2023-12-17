class Solution:
    def Bit(self,number):
        bit=""
        while number:
            kalan=number%2
            bit=str(kalan)+bit
            number=number//2
        return bit
    def countBits(self, n: int) -> List[int]:
        return [self.Bit(i).count("1") for i in range(n+1)]