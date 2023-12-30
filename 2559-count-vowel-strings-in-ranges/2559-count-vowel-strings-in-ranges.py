class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ##### PreProcessing:- Creating prefix sum array of count of valid words
        
        d={"a":1,"e":1,"i":1,"o":1,"u":1}
        preProcess=[0]*(len(words)+1)
        count=0
        for i in range(len(words)):
            if words[i][0] in d and words[i][-1] in d:
                count+=1
            preProcess[i+1]=count      
        
        #### Main Method  #####

        ans=[]
        for i in range(len(queries)):
            start=queries[i][0]
            end=queries[i][1]
            count=preProcess[end+1]-preProcess[start]
            ans.append(count)
        return ans          