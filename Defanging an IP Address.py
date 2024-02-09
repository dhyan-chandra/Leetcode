#Defanging an IP Address

class Solution:
    def defangIPaddr(self, address: str) -> str:
        array = address.split(".")
        new_address = "[.]".join(array)
        return new_address
        


# Example 1:

# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"

# Example 2:
# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"