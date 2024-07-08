public class Solution {
    public string NumberToWords(int number)
    {
        if (number == 0)
        {
            return "Zero";
        }
        if (number >= 0 && number < 20)
        {
            string[] arr = { "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen" };
            return arr[number];
        }
        if (number >= 20 && number < 100)
        {
            string[] arr = { "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety" };
            if (number % 10 == 0)  // Handle cases like 20, 30, ..., 90
            {
                return arr[number / 10 - 2];
            }
            else
            {
                return arr[number / 10 - 2] + " " + NumberToWords(number % 10);
            }
        }
        if (number >= 100 && number < 1000)
        {
            if (number % 100 == 0)  // Handle cases like 100, 200, ..., 900
            {
                return NumberToWords(number / 100) + " Hundred";
            }
            else
            {
                return NumberToWords(number / 100) + " Hundred " + NumberToWords(number % 100);
            }
        }
        if (number >= 1000 && number <= 999999)
        {
            if (number % 1000 == 0)  // Handle cases like 1000, 2000, ..., 999000
            {
                return NumberToWords(number / 1000) + " Thousand";
            }
            else
            {
                return NumberToWords(number / 1000) + " Thousand " + NumberToWords(number % 1000);
            }
        }
        if (number >= 1000000 && number <= 999999999)
        {
            if (number % 1000000 == 0)  // Handle cases like 1000000, 2000000, ..., 999000000
            {
                return NumberToWords(number / 1000000) + " Million";
            }
            else
            {
                return NumberToWords(number / 1000000) + " Million " + NumberToWords(number % 1000000);
            }
        }
        if (number >= 1000000000)
        {
            if (number % 1000000000 == 0)  // Handle cases like 1000000000, 2000000000, ..., etc.
            {
                return NumberToWords(number / 1000000000) + " Billion";
            }
            else
            {
                return NumberToWords(number / 1000000000) + " Billion " + NumberToWords(number % 1000000000);
            }
        }
        
        return "";  // Default case, should not happen given the initial conditions
    }
}
