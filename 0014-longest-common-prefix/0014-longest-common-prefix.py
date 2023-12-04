class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""  # If the input list is empty, there is no common prefix.

        # Find the shortest string in the list (the minimum length determines the common prefix length).
        min_len = min(len(s) for s in strs)
        
        common_prefix = ""
        for i in range(min_len):
            # Compare the current character of all strings with the character at the same position in the first string.
            current_char = strs[0][i]
            for string in strs:
                if string[i] != current_char:
                    return common_prefix  # If characters don't match, return the common prefix found so far.
            
            common_prefix += current_char  # If characters match, add the character to the common prefix.
        
        return common_prefix