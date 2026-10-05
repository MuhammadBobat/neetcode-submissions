class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            count = str(len(s))
            s_encoded = count + '#' + s
            output += s_encoded
        
        return output

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            start = i
            while s[i] != '#':
                i += 1
            length = int(s[start:i])
            start = i + 1
            word = s[start:start + length]
            decoded_strs.append(word)
            i = start + length

        return decoded_strs