class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = re.sub(r"[.]","[.]",address)
        return result