class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        st, end = 0, mountainArr.length() - 1
        while st < end:
            mid = st + (end - st) // 2
            mid_val = mountainArr.get(mid)
            next_val = mountainArr.get(mid + 1)
            if mid_val > next_val:
                end = mid
            else:
                st = mid + 1
        peak = st
        if mountainArr.get(peak) == target:
            return peak
        def find(st, end):
            if st > end:
                return -1
            Flag = mountainArr.get(st) < mountainArr.get(end)
            while st <= end:
                mid = st + (end - st) // 2
                val = mountainArr.get(mid)
                if val == target:
                    return mid
                elif val > target:
                    if Flag:
                        end = mid - 1
                    else:
                        st = mid + 1
                else:
                    if Flag:
                        st = mid + 1
                    else:
                        end = mid - 1
            return -1
        res = find(0, peak - 1)
        if res != -1:
            return res
        return find(peak + 1, mountainArr.length() - 1)