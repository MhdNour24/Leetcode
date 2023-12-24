class Solution:
    def maximum69Number (self, num: int) -> int:
        num=str(num)
        new_number=[]
        for i in range(len(num)):
            if num[i]=="6":
                new_number.append("9")
                try:
                    new_number.append(num[i+1:])
                except:
                    pass
                break
            else:
                new_number.append(num[i])
        
        return int("".join(new_number))