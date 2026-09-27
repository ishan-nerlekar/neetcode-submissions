class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = ""
        for s in strs:
            encoded_strs += s + "IVN"
        return encoded_strs

    def decode(self, s: str) -> List[str]:
        return s.split("IVN")[:-1]