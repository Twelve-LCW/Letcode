class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = [(nums1[i] + nums2[0], i, 0) for i in range(min(len(nums1), k))]
        # nums1 是递增的，无需堆化

        ans = []
        for _ in range(k):
            _, i, j = heappop(h)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans