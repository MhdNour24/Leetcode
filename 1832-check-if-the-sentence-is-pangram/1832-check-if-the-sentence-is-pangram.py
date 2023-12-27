class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
            ref = {v:False for i,v in enumerate('abcdefghijklmnopqrstuvwxyz')}
            for i in sentence: 
                ref[i] = True
            for i in ref: 
                if not ref[i]: 
                    return False
            return True