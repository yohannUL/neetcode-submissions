class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        view = False
        liste = nums.copy()

        for i,x in enumerate(nums):
            if x in liste:
                liste.remove(x)
                if x in liste:
                    view = True

        return view
