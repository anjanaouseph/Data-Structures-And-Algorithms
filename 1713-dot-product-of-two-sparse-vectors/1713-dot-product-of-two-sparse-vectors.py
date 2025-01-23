class SparseVector:
    def __init__(self, nums: List[int]):
        self.v1 = []

        for i,val in enumerate(nums):
            if val:
                self.v1.append((i,val))#add tuples to the list having index and value
   
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0

        i,j=0,0

        while i<len(self.v1) and j<len(vec.v1):
            v1_index, v1_val = self.v1[i]
            v2_index, v2_val = vec.v1[j]

            if v1_index == v2_index:
                result += v1_val * v2_val
                i += 1
                j += 1

            elif v1_index > v2_index:
                j+=1

            else:
                i+=1

        return result

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)