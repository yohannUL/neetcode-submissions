class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        second = ["".join(sorted(s)) for s in strs]

        trois = []

        for i in second:
            if i not in trois :
                trois.append(i)

        for i in  trois:
            d[i] = []
        
        for i in strs:
            sorted_str = "".join(sorted(i))
            if sorted_str in d:
                d[sorted_str].append(i)
            else:
                d[sorted_str] = [i]
        
        return list(d.values())