class Solution {
    getCountOfChars(string, length) {
        const dic = {};
        for (let i = 0; i < length; i++) {
            if (!(string[i] in dic)) {
                dic[string[i]] = 1;
            } else {
                dic[string[i]]++;
            }
        }
        return dic;
    }

    maxLengthOfPalindrome(dic) {
        let counter = 0;
        let isOddNumber = false;
        for (const [char, count] of Object.entries(dic)) {
            if (count % 2 === 1 && !isOddNumber) {
                counter += count;
                isOddNumber = true;
            } else if (count % 2 === 1 && isOddNumber) {
                counter += count - 1;
            } else {
                counter += count;
            }
        }
        return counter;
    }

    longestPalindrome(s) {
        const length = s.length;
        const dic = this.getCountOfChars(s, length);
        return this.maxLengthOfPalindrome(dic);
    }
}

/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {
    const solution = new Solution();
    return solution.longestPalindrome(s);
};
