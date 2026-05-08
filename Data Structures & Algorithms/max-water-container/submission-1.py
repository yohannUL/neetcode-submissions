class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        aire = 0

        gauche = 0
        droite = len(heights)-1

        while gauche < droite :
            largeur = droite - gauche
            hauteur = min(heights[gauche], heights[droite])
            aire = hauteur *largeur

            if aire > result:
                result = aire

            if heights[gauche]>heights[droite]:
                droite -= 1

            else:
                gauche += 1

        return result 
