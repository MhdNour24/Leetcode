class Solution:
    def secondHighest(self, s: str) -> int:
        int_list=[]
        for i in s:
            if i.isdigit() and int(i) not in int_list:
                int_list.append(int(i))
        int_list.sort()
        try:
            return int_list[-2]
        except:
            return -1
