class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points=sorted(points,reverse=True)
        # points=points[::-1]
        a=points[0]
        arrows=1
        for point in points:
            if a[0]<=point[1]:
                pass
            else:
                a=point
                arrows+=1
        return arrows