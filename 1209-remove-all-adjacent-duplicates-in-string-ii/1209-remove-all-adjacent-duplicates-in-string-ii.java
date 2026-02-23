class Solution {
    public String removeDuplicates(String s, int k) {

        if (s.length() == 0)
        return "";

        Stack<int[]> stack = new Stack();

        for (char c : s.toCharArray())
        {
            if (!stack.isEmpty() && stack.peek()[0] == c)
            {
                stack.peek()[1]++;
            }
            else
            {
                stack.push(new int[]{c, 1});//c gets stored as integer and not char
            }

            if (stack.peek()[1] == k)
            {
                stack.pop();
            }
        }

        //rebuild string from stack
        StringBuilder res = new StringBuilder();

        for (int [] pair : stack)
        {
            char c = (char)pair[0];
            int count = pair[1];

            for (int i = 0; i<count; i++)
                res.append(c);
            
        }

        return res.toString();
        
    }
}