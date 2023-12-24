class Solution:
    def numSubmat(self, A):
        ans, m, n = 0, len(A), len(A[0])
        for i in range(m):
            stack = [-1]
            A[i].extend([0, -1])
            for j in range(n + 1):
                if i and A[i][j]: A[i][j] += A[i - 1][j]
                while stack and A[i][stack[-1]] >= A[i][j]:
                    h = A[i][stack.pop()] - max(A[i][j], A[i][stack[-1]])
                    w = j - stack[-1] - 1
                    ans += ((w * (w + 1)) >> 1) * h
                stack.append(j)
        return ans