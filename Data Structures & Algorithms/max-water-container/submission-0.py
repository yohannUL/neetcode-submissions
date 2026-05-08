class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        result_intermediare = 0

        for x ,valx in enumerate(heights):
            for y ,valy in enumerate(heights):
                if x != y:
                    result_intermediare = min(valx,valy) * abs((y -x))
                    if result_intermediare > result:
                        result =result_intermediare
                        print(result)



        return result
