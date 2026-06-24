class Solution:

    def encode(self, strs: List[str]) -> str:
        coded=""
        for s in strs:
            coded=coded+s+'.'
        return coded

    def decode(self, s: str) -> List[str]:
        return s.split('.')[:-1]