class Solution:
    def findLexSmallestString(self, s, a, b) :
        # add and rotate function
        def add(s,a):
            new = ""
            for i in range(len(s)):
                if i % 2 != 0:
                    new += str(int(s[i])+a)[-1]
                else:
                    new += s[i]
            return new
        
        def rotate(s,b):
            return s[len(s)-b:]+s[:len(s)-b] 
        
        # Perform search         
        seen = set()
        need = list()
        need.append(s)

        while need:
            curr = need.pop()
            if curr not in seen:
                # add current string to seen                 
                seen.add(curr)
                # add next two cases into waiting queue
                need.extend([add(curr,a),rotate(curr,b)])
                
        # select smallest string from all possible cases        
        return min(seen)