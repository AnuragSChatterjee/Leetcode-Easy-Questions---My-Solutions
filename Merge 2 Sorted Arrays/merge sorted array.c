class Solution(object):
    def merge(self, nums1, m, nums2, n) 
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        int i = m-1;
        int j = n-1;
        int k = m+n-1;

        while (j>=0) {
              if (i>=0 && nums1[i] > nums2[j] {
                  nums1[k--] = nums1[i--];
              }
              else {
                  nums1[k--] = nums2[j--];
              }
        }

      

