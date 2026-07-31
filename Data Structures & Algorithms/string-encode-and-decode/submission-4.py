class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for a in strs:
            result += str(len(a)) + "#" + a

        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        length_s = len(s)
        result = []

        print(s)
        while i < length_s:
            j = s.find("#", i)
            length = int(s[i:j])
            result.append(s[j+1:j+1+length])
            i = j+1+length

        return result


