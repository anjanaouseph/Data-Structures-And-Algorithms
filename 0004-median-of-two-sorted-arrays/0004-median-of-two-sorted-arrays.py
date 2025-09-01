class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1)> len(nums2):
            return self.findMedianSortedArrays(nums2, nums1) #smallest array should be nums1

        n1 = len(nums1)
        n2 = len(nums2)

        left = 0
        right = n1

        total = n1+n2
        half = (total+1)//2

        while left<=right:
            mid1 = (left+right)//2 #no of elements to take from mid1
            mid2 = half-mid1  #no of elements to take from mid2
            
            l1 = nums1[mid1 - 1] if mid1 > 0 else float('-inf')
            r1 = nums1[mid1]     if mid1 < n1 else float('inf')
            l2 = nums2[mid2 - 1] if mid2 > 0 else float('-inf')
            r2 = nums2[mid2]     if mid2 < n2 else float('inf')

            #check symmetry
            if l1<=r2 and l2<=r1:
                if total%2 == 0:
                    return (max(l1,l2)+min(r1,r2))/2.0
                else:
                    return max(l1,l2)

            elif l1>r2:
                right = mid1-1
            else:
                left = mid1+1