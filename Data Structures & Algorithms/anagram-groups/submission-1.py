class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        liste =[]

        for mot in strs:
            mot_sorted = "".join(sorted(mot))

            if mot_sorted in anagrams:
                anagrams[mot_sorted].append(mot)

            else:
                anagrams[mot_sorted] = [mot]


        for groupe in anagrams.values():
            liste.append(groupe)


        return liste