class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vus = {}

        for indice, nombre in enumerate(nums):
            partenaire = target - nombre

            if partenaire in vus:
                return [vus[partenaire], indice]

            else:
                vus[nombre] =indice


        return [1,1]