from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:

    smalla = nums1[0:m] 
    smallb = nums2[0:n]

    i = 0  
    j = 0
    k = 0
    while(i<len(smalla) and j<len(smallb)):
        if (smalla[i] <= smallb[j]):
            nums1[k] = smalla[i]
            i+=1
        else:
            nums1[k] = smallb[j]
            j+=1
        k+=1
    while i<len(smalla):
        nums1[k] = smalla[i]
        i+=1
        k+=1
    while j<len(smallb):
        nums1[k] = smallb[j]
        j+=1
        k+=1
  

nums1 = []
nums2 = []
for item in input().split(', '):
  nums1.append(int(item))
for item in input().split(', '):
  nums2.append(int(item))
m = int(input())
n = int(input())
merge(nums1, m, nums2, n)
print(nums1)
