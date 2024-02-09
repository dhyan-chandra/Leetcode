#Unique Morse Code Words

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = []
        for word in words:
            morse = ""
            for char in word:
                morse = morse + morse_code[ord(char)-97]
            if morse not in res:
                res.append(morse)
        return(len(res))
        



#Example 1:
#Input: words = ["gin","zen","gig","msg"]
#Output: 2
#Explanation: The transformation of each word is:
#"gin" -> "--...-."
#"zen" -> "--...-."
#"gig" -> "--...--."
#"msg" -> "--...--."
#There are 2 different transformations: "--...-." and "--...--.".

#Example 2:
#Input: words = ["a"]
#Output: 1