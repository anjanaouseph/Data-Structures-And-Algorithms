class Solution {
    public int firstUniqChar(String s) {

        HashMap <Character, Integer> hashMap = new HashMap<>();

        //build hashMap
        for (int i = 0; i < s.length(); i++)
        {
            char c = s.charAt(i);//cant use s[i] as its string object not array
            hashMap.put(c, hashMap.getOrDefault(c, 0) + 1);

        }

        //iterate again
        for (int i = 0; i<s.length(); i++)
        {   
            if (hashMap.get(s.charAt(i)) == 1) 
            {
                return i;
            }
            
        }

        return -1;
    }
}

// TC: O(N)
// SC: O(26) -> O(1) //as only smaller case allowed