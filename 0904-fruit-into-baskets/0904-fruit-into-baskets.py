class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        curr_type = fruits[0]
        curr_index = 0
        other_type = None
        strike = 1
        result = 0

        for i in range(1, n):
            new_type = fruits[i]
            if new_type == curr_type:
                strike += 1
            elif new_type == other_type:
                strike += 1
                curr_type, other_type = other_type, curr_type
                curr_index = i
            else:
                result = max(result, strike)
                strike = i - curr_index + 1
                curr_index = i
                curr_type, other_type = new_type, curr_type
        
        result = max(result, strike)
        return result


