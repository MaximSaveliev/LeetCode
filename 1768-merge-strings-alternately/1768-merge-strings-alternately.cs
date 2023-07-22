public class Solution {
    public string MergeAlternately(string word1, string word2)
    {
        int len1 = word1.Length;
        int len2 = word2.Length;

        // Use StringBuilder to efficiently build the merged string
        StringBuilder stringBuilder = new StringBuilder();

        for (int i = 0; i < len1 + len2; i++)
        {
            if (i < len1)
                stringBuilder.Append(word1[i]);
            if (i < len2)
                stringBuilder.Append(word2[i]);
        }

        return stringBuilder.ToString();
    }
}