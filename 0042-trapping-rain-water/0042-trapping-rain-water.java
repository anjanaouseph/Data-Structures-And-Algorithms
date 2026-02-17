class Solution {
    public int trap(int[] height) {

        //note maxleft and maxright won't decrease if u move inwards, they can only increase

        int n = height.length;
        int i = 0;
        int j = n-1;

        int max_left = height[i];
        int max_right = height[j];

        int count = 0;
        int res = 0;

        while (i < j)
        {
            if (max_left <= max_right)
            {
                i++; //we found the limiting boundary for next index
//I move the smaller side because the smaller boundary determines the water level; the other side is guaranteed to be at least as tall
//basically iam moving this because ik this ans won't change later in the future.
                res = Math.min(max_left, max_right)-height[i];

                if (res > 0)
                    count += res;

                max_left = Math.max(height[i], max_left);
            }
            else
            {
                j--;

                res = Math.min(max_left, max_right)-height[j];

                if (res > 0)
                    count += res;

                max_right = Math.max(height[j], max_right);


            }
        }


        return count;
        
    }
}