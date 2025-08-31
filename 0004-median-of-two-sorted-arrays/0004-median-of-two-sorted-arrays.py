class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A, B = nums1, nums2

        if len(A) > len(B):           # ensure A is the smaller array
            A, B = B, A

        total = len(A)+len(B)

        half = total//2

        left = 0
        right = len(A)-1

        while True:
            mid = (left+right)//2
            mid2 = half - mid - 2

            Aleft = A[mid] if mid >= 0 else float("-infinity")
            Aright = A[mid+1] if mid+1 < len(A) else float("infinity")

            Bleft = B[mid2] if mid2 >= 0 else float("-infinity")
            Bright = B[mid2+1] if mid2+1 < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total%2 == 0:#check if even no
                    return (max(Aleft, Bleft)+min(Aright, Bright))/2
                else:#if no of elements are odd
                    return min(Aright, Bright)
            elif Aleft>Bright:
                right = mid-1
            else:
                left = mid+1     

        return left