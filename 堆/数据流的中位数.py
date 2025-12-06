from heapq import heappush, heappushpop


class MedianFinder:
    def __init__(self):
        self.left = []  # 入堆的元素取相反数，变成最大堆
        self.right = []  # 最小堆

    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
            heappush(self.left, -heappushpop(self.right, num))
        else:
            heappush(self.right, -heappushpop(self.left, -num))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (self.right[0] - self.left[0]) / 2


class MedianFinder:

    def __init__(self):
        #左边存小的一半，右边存大的一半
        self.right=[] #小顶堆 第一个数是最小的数
        self.left=[] #大顶堆 第一个数是最大的 python没有大顶堆 可以小顶堆存入负数当作小顶堆
        

    def addNum(self, num: int) -> None:
        if len(self.left)==len(self.right): 
            #如果左右两边现在数量相等，新来的先进右边，再从右边挪一个最小的去左边
            heappush(self.left,-heappushpop(self.right,num))
        else:
            #如果左右两边现在数量不等（左>右），新来的先进左边，再从右边挪一个最小的去右边
            heappush(self.right,-heappushpop(self.left,-num))
        

    def findMedian(self) -> float:
        #左>右，左边最大的就是中位数
        if len(self.left)>len(self.right):
            return -self.left[0]
        #左=右，左边最大+右边最小 /2
        return (self.right[0]-self.left[0])/2