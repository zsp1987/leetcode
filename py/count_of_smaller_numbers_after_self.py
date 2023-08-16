class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [(v, i) for i, v in enumerate(nums)]
        result = [0] * n

        def merge_sort(arr, left, right):
            if right - left <= 1:
                return
            mid = (left + right) // 2
            merge_sort(arr, left, mid)
            merge_sort(arr, mid, right)
            merge(arr, left, right, mid)

        def merge(arr, left, right, mid):
            l = left
            r = mid
            temp = []
            while l < mid and r < right:
                if arr[l][0] <= arr[r][0]:
                    result[arr[l][1]] += r - mid
                    temp.append(arr[l])
                    l += 1
                else:
                    temp.append(arr[r])
                    r += 1
            while l < mid:
                result[arr[l][1]] += r - mid
                temp.append(arr[l])
                l += 1
            while r < right:
                temp.append(arr[r])
                r += 1
            for i in range(left, right):
                arr[i] = temp[i - left]

        merge_sort(arr, 0, n)
        return result
