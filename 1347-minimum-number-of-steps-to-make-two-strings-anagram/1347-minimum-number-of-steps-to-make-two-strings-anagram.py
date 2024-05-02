class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter=0
        dic_s=Counter(s)
        dic_t=Counter(t)
        for item,count in dic_s.items():
            if item in dic_t:
                a=count-dic_t[item]
                if a>=0:
                    counter+=a
            else:
                counter+=count
        return counter