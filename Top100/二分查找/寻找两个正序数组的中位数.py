class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        def getKthElement(k):
            index1,index2=0,0
            while True:
                if index1==m:
                    return nums2[index2+k-1]
                if index2==n:
                    return nums1[index1+k-1]
                if k==1:
                    return min(nums1[index1],nums2[index2])
                
                newIndex1=min(index1+k//2-1,m-1)
                newIndex2=min(index2+k//2-1,n-1)
                pviot1,pvoit2=nums1[newIndex1],nums2[newIndex2]
                if pviot1<=pvoit2:
                    k-=newIndex1-index1+1
                    index1=newIndex1+1
                else:
                    k-=newIndex2-index2+1
                    index2=newIndex2+1
        totalLength=m+n
        if totalLength%2==1:
            return getKthElement((totalLength+1)//2)
        else:
            return (getKthElement(totalLength//2)+getKthElement(totalLength//2+1))/2

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 确保nums1是较短的数组
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            
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