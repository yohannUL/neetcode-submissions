class Solution:
    def isPalindrome(self, s: str) -> bool:
        liste =[]
        
        reponse = True

        for i in s:
            if  i.isalpha() or i.isalnum():
                i = i.lower()
                liste.append(i)

        long = len(liste)
        
        print(liste)



        for i in range(long ):
            if liste[i] != liste[long -i-1] :
                reponse = False
                break

        return reponse