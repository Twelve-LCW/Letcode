class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 确保nums1是较短的数组
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        
        while imin <= imax:
            i = (imin + imax) // 2 #nums1的切割位置
            j = half_len - i #nums2的切割位置
            
            # 处理边界情况
            if i < m and nums2[j-1] > nums1[i]:
                # i太小，需要增大
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # i太大，需要减小
                imax = i - 1
            else:
                # 找到合适的分割线，处理中位数计算
                
                # 计算左半部分最大值
                if i == 0:
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])
                
                # 如果总数是奇数，直接返回左半部分最大值
                if (m + n) % 2 == 1:
                    return max_of_left
                
                # 计算右半部分最小值
                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                
                # 如果是偶数，返回平均值
                return (max_of_left + min_of_right) / 2.0


class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        if len(a) > len(b):
            a, b = b, a  # 保证下面的 i 可以从 0 开始枚举

        m, n = len(a), len(b)
        a = [-inf] + a + [inf]
        b = [-inf] + b + [inf]

        # 枚举 nums1 有 i 个数在第一组
        # 那么 nums2 有 j = (m + n + 1) // 2 - i 个数在第一组
        i, j = 0, (m + n + 1) // 2
        while True:
            if a[i] <= b[j + 1] and a[i + 1] > b[j]:  # 写 >= 也可以
                max1 = max(a[i], b[j])  # 第一组的最大值
                min2 = min(a[i + 1], b[j + 1])  # 第二组的最小值
                return max1 if (m + n) % 2 else (max1 + min2) / 2
            i += 1  # 继续枚举
            j -= 1