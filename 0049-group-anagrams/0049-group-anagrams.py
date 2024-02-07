class Solution:
    def sort_char(self,s):
        ls = sorted(s)
        ans = ''.join(ls)
        return ans
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        matrix=[]
        c=0
        dic={}
        for i in strs:
            new_str=self.sort_char(i)
            if new_str not in dic:
                dic[new_str]=c
                c+=1
                matrix.append([i])
            else:
                hash_value=dic[new_str]
                matrix[hash_value].append(i)
        return matrix