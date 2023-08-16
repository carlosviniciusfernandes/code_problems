# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

#! does not meet O(log(m+n))
class Solution1:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        arr = sorted([*nums1, *nums2])

        length = len(arr)
        if length % 2 == 0:
            index1, index2 = int(length/2-1), int(length/2)
            return (arr[index1] + arr[index2]) / 2
        else:
            index=int((length-1)/2)
            return arr[index]

class Solution2:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # A
            j = half - i - 2  # B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1