class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result =0
        gauche = 0
        droite = 1

        while droite < len(prices):
            prix_inter = prices[droite] - prices[gauche]

            if prix_inter > result:
                result = prix_inter

            if prices[droite] < prices[gauche]:
                gauche = droite

            droite += 1
                


        return result