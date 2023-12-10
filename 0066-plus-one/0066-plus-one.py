class Solution(object):
    def plusOne(self, digits):
        kelime=""
        for i in digits:
            kelime+=str(i)
        kelime=int(kelime)
        kelime+=1
        return list(map(int," ".join(str(kelime).split())))
        