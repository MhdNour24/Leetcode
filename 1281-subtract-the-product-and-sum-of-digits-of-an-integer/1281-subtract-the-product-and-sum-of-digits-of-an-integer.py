class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum=0
        product=1
        while n>0:
            last_digit=n%10
            n=int((n-last_digit)/10)
            sum+=last_digit
            product*=last_digit
        return product-sum
                