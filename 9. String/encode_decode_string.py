exec(open('out.py').read())

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        res = ""
        for item in strs:
            res += str(len(item)) + '#' + item
        return res

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, encoded_str):
        # write your code here
        res = []
        i, j = 0, 0
        while i < len(encoded_str):
            while encoded_str[j] != '#':
                j += 1
            length = int(encoded_str[i : j])
            res.append(encoded_str[j+1 : j+1+length])
            i = j + length + 1
            j = j + length + 1


        return res



print(Solution().decode(Solution().encode(["we", "say", ":", "yes"])))
