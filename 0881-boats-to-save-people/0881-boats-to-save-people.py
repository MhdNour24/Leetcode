class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        counter=0
        length=len(people)
        start=0
        end=length-1
        while start<=end:
            if start!=end:
                toplam=people[start]+people[end]
            else:
                toplam=people[start]
            if toplam<=limit:
                counter+=1
                start+=1
                end-=1
            else:
                counter+=1
                start+=1
            
        return counter
        