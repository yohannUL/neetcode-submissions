class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = ""

        for mot in strs:
            encoded_string += str(len(mot)) + "#" +mot

        return encoded_string

    def decode(self, s: str) -> List[str]:
        resultat = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            longueur = int(s[i:j])

            debut = j + 1
            fin = debut + longueur

            mot = s[debut:fin]
            resultat.append(mot)

            i = fin

        return resultat