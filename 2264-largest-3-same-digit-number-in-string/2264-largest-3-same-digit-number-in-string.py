class Solution:
    def largestGoodInteger(self, num: str) -> str:
        if not num:
            return ""
        count=1
        length=len(num)
        last_number=num[0]
        large_integer=None
        t=False
        for i in range(1,length):
            number=num[i]
            if number==last_number:
                count+=1
                if count==3:
                    k=number+number+number
                    if large_integer==None:
                        large_integer=k
                    else:
                        if int(k)>int(large_integer):
                            large_integer=k

                    t=True
                    count=1
            elif number !=last_number or t:
                last_number=number
                count=1
        if large_integer==None:
            return ""
        else:
            return large_integer
