class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nombre = set()

        for i in nums:
            if i in nombre:
                return True
            else:
                nombre.add(i)

        return False

