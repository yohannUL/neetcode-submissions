class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dico = {}

        for n in nums:
            if n in dico:
                dico[n] += 1
            else:
                dico[n] = 1

        sorted_dico = sorted(dico.items(), key=lambda x: x[1], reverse=True)

        result = []

        for key, value in sorted_dico[:k]:
            result.append(key)

        return result