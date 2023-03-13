class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        finalresult = []
        nums1_sorted = sorted(nums1)
        nums2_sorted = sorted(nums2)
        i = 0
        j = 0
        while len(nums1_sorted) > i and len(nums2_sorted) > j:
            if nums1_sorted[i] == nums2_sorted[j]:
                result.append(nums1_sorted[i])
                i+=1 
                j+=1
            elif nums1_sorted[i] > nums2_sorted[j]:
                j+=1
            elif nums1_sorted[i] < nums2_sorted[j]:
                i+=1
        return sorted(result)