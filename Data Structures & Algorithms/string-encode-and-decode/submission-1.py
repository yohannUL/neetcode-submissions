class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string =[]
        
        for i in strs:
            encoded_string.append("#@")
            #encoded_string.append(str(len(i)))
            encoded_string.append(i)

        encoded_string = "".join(encoded_string)


        print(encoded_string)
    
        return encoded_string;

    def decode(self, s: str) -> List[str]:

        strs = s.split("#@")
        strs.pop(0)


        return strs;
