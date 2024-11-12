class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1#swap arrays if n1>n2, we work on the smallest array to reduce time complexity
        n1 = len(nums1)
        n2 = len(nums2)
        half = (n1+n2+1)//2 ## length of left half works for both even and odd no size eg (10+1)//2 is same as 10///2 which is #5
        #applying binary search to find the no. of elements we need from first array's left part
        left, right = 0, n1
        while left <= right:
            mid1 = (left+right)//2
            mid2 = half-mid1
            #find l1,l2,r1,r2
            l1,l2,r1,r2 = float('-inf'), float('-inf'), float('inf'), float('inf')
            #now check edge cases, so as not to get index oob exception
            if mid1-1>=0:#check if the element exist
                l1 = nums1[mid1-1]
            if mid2-1>=0:
                l2 = nums2[mid2-1]
            if mid1 < n1:#only if the element exist
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]

            #check for symmetry from both the halves of the 2 arrays
            if l1<=r2 and l2<=r1:#if this matches we have got the left and right halves of the meregd array
                if (n1+n2)%2 == 0:#find median if even no of elements
                    return (max(l1,l2)+min(r1,r2))/2.0
                else:
                    return max(l1,l2)

            elif l1>r2:
                right = mid1-1 #pick less elements from array 1
            else:
                left = mid1+1 #if l2>r1 pick more elements from first array 1

        return 0.0