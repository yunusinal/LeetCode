"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right,
and replace the last element with -1. After doing so, return the array.

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.

"""

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rvrsd_arr=[-1]
        max_val=0 
        for num in arr[::-1]: # 1,6,5,4,18,17 
            if max_val < num:
                max_val = num
            rvrsd_arr.append(max_val)    
        return rvrsd_arr[-2::-1]  # tekrar terse döndürüp son elemanını almıyoruz