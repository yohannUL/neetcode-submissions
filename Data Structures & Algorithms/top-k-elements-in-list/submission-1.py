class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequence = {}
        result =[]

        for nombre in nums:
            if nombre in frequence:
                frequence[nombre] += 1

            else:
                frequence[nombre] = 1

        
        nombre_tries = sorted(frequence, key=frequence.get,reverse=True)

        for i in range(k):
            result.append(nombre_tries[i])

        return result