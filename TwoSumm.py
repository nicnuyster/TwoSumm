import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#print(os.getcwd())
#from misc.Sortings import Sorts
#import time

class TSSolution():

    # Easiest + worst case O(n^2)
    def SimpleSumma(nums, target):
        for i in range(len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return "Zero solutions???"
    
    # Ideal O(n) or O(ChatGPT)
    def Mappe(nums, target):
        num_mappe = {}

        for i, num in enumerate(nums):
            # compliment is like join in SQL
            compliment = target - num
            if compliment in num_mappe:
                return [num_mappe[compliment], i]
            num_mappe[num] = i
        return "Zero solutions???"

    # O(n) for sorted array     
    def TwoPointers(nums, target):

        p1 = 0
        p2 = len(nums)-1
        SortObj = Sorts()

        # My sort
        nums = SortObj.quicksortMy(nums)

        while p1 != p2:
            if nums[p1] + nums[p2] == target:
                return [p1, p2]
            p2 -= 1
        return "Zero solutions???"

if __name__ == "__main__":
    
#Data
    #arrays
    nums1 = [1, 2, 3, 4, 5, 6]
    nums2 = [5, 2, 1, 5, 7, 4]
    nums3 = [1, 1, 1, 1, 1]
    nums4 = [1]
    nums5 = ['a','b','c']
    nums6 = []
    #targets
    targ1 = 0
    targ2 = 1
    targ3 = 2
    targ4 = 3
    targ5 = 'a'

#tests different things ++
    print("simple tests + exc time", '\n')

    print("simple")
    # simple
    start_time = time.perf_counter()
    otv1 = TSSolution.SimpleSumma(nums1, targ4)
    end_time = time.perf_counter()
    print(f"1 time - {end_time - start_time:.6f}s")
    print("1 val - ", otv1, '\n')

    print("map")
    # map
    start_time = time.perf_counter()
    otv1 = TSSolution.Mappe(nums1, targ4)
    end_time = time.perf_counter()
    print(f"1 time - {end_time - start_time:.6f}s")
    print("1 val - ", otv1, '\n')

    print("2p")
    # 2p
    start_time = time.perf_counter()
    otv1 = TSSolution.TwoPointers(nums1, targ4)
    end_time = time.perf_counter()
    print(f"1 time - {end_time - start_time:.6f}s")
    print("1 val - ", otv1, '\n')