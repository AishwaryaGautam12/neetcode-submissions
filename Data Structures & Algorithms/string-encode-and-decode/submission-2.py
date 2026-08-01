class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ''
        for s in strs:
            output += str(len(s))+'#'+s

        return output

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            length = ''
            while s[i] != '#':
                length += s[i]
                i += 1

            i = i+1
            count = 0
            string = ''
            while count != int(length):
                string += s[i]
                count += 1
                i += 1
            output.append(string)

        return output


