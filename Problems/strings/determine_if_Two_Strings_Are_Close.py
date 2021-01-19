class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if "".join(sorted(word1)) == "".join(sorted(word2)):
            return True
        else: 
            c1,c2=[],[]
            set_word1=set(word1)
            set_word2=set(word2)
            if not set_word1 == set_word2:
                return False
            for i in set_word1:
                c1.append(word1.count(i))
            for i in set_word2:
                c2.append(word2.count(i))
            if not sorted(c1) == sorted(c2):
                return False   
            
        return True
