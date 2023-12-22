class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
	# runtime: 38ms
        if not A or not B:
            return False
        if A == B:
            return True
        if len(A)!=len(B):
            return False
        
        for i in range(len(A)):
            if (A[i:len(A)]+A[0:i]) == B:
                return True
        return False