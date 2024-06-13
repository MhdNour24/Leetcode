class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        coutOfMovies=0
        for i in range(len(seats)):
            coutOfMovies+=abs(seats[i]-students[i])

        return coutOfMovies