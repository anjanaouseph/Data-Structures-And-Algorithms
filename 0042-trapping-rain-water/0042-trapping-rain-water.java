class Solution {
    public int trap(int[] height) {

        int n = height.length;
        int i = 0;
        int j = n-1;
        int max_left = height[i];
        int max_right = height[j];

        int res = 0;
        int count = 0;

// maxLeft  = tallest wall seen so far from the LEFT side for any position at/inside i
// maxRight = tallest wall seen so far from the RIGHT side for any position at/inside j
        while (i < j) //when i == j, nothing to trap, no cavity
        {
            if (max_left <= max_right)
            {
                i ++ ;//helps eliminate the edge cases when there are no boundaries as well
                //we found the limiting height on left side now compute the water capacity for next index
                res = Math.min(max_left, max_right)-height[i];

                if (res > 0)
                    count += res;

                max_left = Math.max(max_left, height[i]);
                

            }
            else
            {
                j --;
                res = Math.min(max_left, max_right)-height[j];
                if (res>0)
                    count += res;

                max_right = Math.max(max_right, height[j]);
            }
        }
        
        return count;
    }
}