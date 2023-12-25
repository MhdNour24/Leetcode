# Define a class called Solution.
class Solution:
    # Define a method called getWinner that takes an array 'arr' and an integer 'k' as inputs.
    def getWinner(self, arr: List[int], k: int) -> int:
        # Calculate the length of the input array and store it in 'n'.
        n = len(arr)
        
        # Check if the length of the array is less than or equal to 'k'.
        if n <= k:
            # If so, return the maximum value in the array as the winner.
            return max(arr)
        
        # Initialize variables to keep track of the count of consecutive wins and the current winner.
        count = 0
        winner = arr[0]
        
        # Iterate through the elements of the array starting from the second element.
        for x in arr[1:]:
            # Check if the current element 'x' is greater than the current winner.
            if x > winner:
                # If 'x' is greater, update the winner to 'x' and reset the count to 1.
                winner = x
                count = 1
            else:
                # If 'x' is not greater, increment the count.
                count += 1
            
            # Check if the count has reached 'k'.
            if count == k:
                # If so, break out of the loop.
                break
        
        # Return the winner after the loop completes.
        return winner

        return winner
