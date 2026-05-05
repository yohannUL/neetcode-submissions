class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = False
        first = []
        second = []

        for i in s:
            first.append(i)

        for i in t:
            second.append(i)

        first.sort()
        second.sort()

        a = len(first)

        b = len (second)

        if a  != b:
            return result

        if first == second:
            return not result

        return result