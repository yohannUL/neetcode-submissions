class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_liste = []
        for i in t:
            t_liste.append(i)

        for i in s:
            if i in t_liste:
                t_liste.remove(i)

            else:
                return False
        if len(t_liste) != 0:
            return False
        return True
