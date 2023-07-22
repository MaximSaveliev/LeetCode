public class Solution {
    public string GcdOfStrings(string str1, string str2)
    {
        if (str1.Length < str2.Length)
        {
            // Swap str1 and str2 to ensure str1 is not shorter than str2
            return GcdOfStrings(str2, str1);
        }

        if (str1.StartsWith(str2))
        {
            // If str1 starts with str2, we check if the remaining part of str1 is divisible by str2
            string remainingStr = str1.Substring(str2.Length);
            return remainingStr.Length == 0 ? str2 : GcdOfStrings(str2, remainingStr);
        }

        return string.Empty; // If there is no common prefix, return an empty string
    }
}