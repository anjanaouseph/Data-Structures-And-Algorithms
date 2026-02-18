//We can see in merged array some elements on left are from arr 1 and some are from arr 2
//1. we do BS based on symmetry, i.e how many from arr1 on left and how many from arr2 on left (lly on right side as well)
//2. how to check if the symm is valid or not? we do criss cross check
//3. find the median (odd and even case)

class Solution
{
    public double findMedianSortedArrays(int[] nums1, int[] nums2)
    {
        if (nums1.length > nums2.length)
            return findMedianSortedArrays(nums2, nums1);

        int n1 = nums1.length;
        int n2 = nums2.length;

        int left_half = (n1+n2+1)/2; //floor division

        int left = 0;
        int right = n1;

        while (left <= right)
        {
            int mid1 = (left + right)/2;
            int mid2 = left_half - mid1;

            int l1 = (mid1>0)? nums1[mid1-1] : Integer.MIN_VALUE;
            int l2 = (mid2>0)? nums2[mid2-1] : Integer.MIN_VALUE;
            int r1 = (mid1 < n1)? nums1[mid1] : Integer.MAX_VALUE;
            int r2 = (mid2 < n2)? nums2[mid2] : Integer.MAX_VALUE;

            //check if symmetry is satisfied?
            if (l1 <= r2 && l2 <= r1)
            {
                if ((n1+n2)%2 == 0)
                {   
                    return (Math.max(l1,l2)+Math.min(r1,r2))/2.0;

                }
                else //odd case
                {
                    return Math.max(l1,l2);
                }
            }

            if (l1 > r2)//we took more elements from arr1, reduce it
                right = mid1-1;
            else
                left = mid1+1;

        }
            return 0.0;     

    }
}