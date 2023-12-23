class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_address=""
        for i in range(len(address)):
            if address[i]==".":
                new_address+="[.]"
                continue
            new_address+=address[i]
        return new_address