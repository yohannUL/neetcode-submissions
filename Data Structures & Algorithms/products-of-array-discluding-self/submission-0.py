class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        inter = nums.copy()
        resultat =[]


        for i,val in enumerate(nums):
            inter.pop(i)
            total = 1
            for i in inter:
                total = total * i
            resultat.append(total)
            inter = nums.copy()

        return resultat


