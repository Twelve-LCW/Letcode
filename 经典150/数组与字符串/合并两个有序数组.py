class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3=nums1[:m]
        l=r=0
        index=0
        while l<m and r<n:
            if nums3[l]<=nums2[r]:
                nums1[index]=nums3[l]
                l+=1
            else:
                nums1[index]=nums2[r]
                r+=1
            index+=1
        nums1[index:m+n]=nums2[r:] if l==m else nums3[l:]

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2, p = m - 1, n - 1, m + n - 1
        while p2 >= 0:  # nums2 还有要合并的元素
            # 如果 p1 < 0，那么走 else 分支，把 nums2 合并到 nums1 中
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]  # 填入 nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]  # 填入 nums2[p1]
                p2 -= 1
            p -= 1  # 下一个要填入的位置