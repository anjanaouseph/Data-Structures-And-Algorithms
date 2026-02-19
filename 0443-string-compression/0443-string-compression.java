class Solution
{
    public int compress(char [] chars)
    {
        int i = 0; 
        int k = 0; //write into the array
        int n = chars.length;

        while (i < n)
        {
            int j = i+1;

            while (j < n && chars[j] == chars[i])
            {
                j++;
            }

            int count = j-i;

            chars[k] = chars[i];
            k++;

            if (count > 1)
            {
                String countString = String.valueOf(count);//convert to string
                for (char ch : countString.toCharArray()) //string is not iterable as char
                {
                    chars[k++] = ch;

                } 

            }
            i = j;
            
        }

        return k;
    }
}