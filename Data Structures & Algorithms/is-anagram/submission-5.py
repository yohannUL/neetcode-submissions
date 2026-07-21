class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        compteur_s = {}
        compteur_t = {}

        for lettre in s:
            compteur_s[lettre] = compteur_s.get(lettre,0) +1

        for lettre in t:
            compteur_t[lettre] = compteur_t.get(lettre,0) + 1

        return compteur_s == compteur_t