#To Lower Case

class Solution:
    def toLowerCase(self, s: str) -> str:
        output = []
        for i in s:
            if i.isupper():
                output.append(chr(ord(i)+32))
            else:
                output.append(i)
        return "".join(output)
        
        
# diffrence between uppar case and lower case of two characters is 32