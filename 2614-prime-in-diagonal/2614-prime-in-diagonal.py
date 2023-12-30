class Solution:
    def prime_number(self,num):
        if num==1:
            return False
        for i in range(2,int(pow(num,0.5))+1):
            if num%i==0:
                return False
        return True

        
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        ind2=len(nums[0])-1
        max_prime=None
        for i in range(len(nums)):
            num1=nums[i][i]
            if self.prime_number(num1):
                if not max_prime:
                    max_prime=num1
                else:
                    max_prime=max(max_prime,num1)
            num2=nums[i][ind2]
            ind2-=1
            if self.prime_number(num2):
                if not max_prime:
                    max_prime=num2
                else:
                    max_prime=max(max_prime,num2)
        if not max_prime:
            return 0
        return max_prime