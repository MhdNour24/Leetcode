class Solution(object):
    def addDigits(self, num):
        if num<10:
            return num
        else:
            toplam=0
            sayistr=str(num)
            for i in sayistr:
                toplam+=int(i)
            return self.addDigits(toplam)