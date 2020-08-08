# Design a data structure that supports the following two operations:
#
# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.
#
# Example:
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# Note:
# You may assume that all words are consist of lowercase letters a-z.
#



class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trieDs = {}

    def insert(self, word):
        x = self.trieDs

        for ind, i in enumerate(word):
            if i not in x:
                x[i] = {"val": {}, "isleaf": ind == len(word) - 1}
                x = x[i]["val"]
            else:
                x = x[i]["val"]

    def searchDs(self, word, rtrieDs):
        x = rtrieDs

        if not x:
            return False

        for ind, i in enumerate(word):
            if i not in x and i != '.':
                return False
            else:
                if (ind == len(word) - 1):
                    if i == '.':
                        for j in x:
                            if x[j]["isleaf"]:
                                return True
                        return False

                    elif x[i]["isleaf"]:
                        return True
                    else:
                        return False

                if i == '.':
                    for j in x:
                        if self.searchDs(word[ind + 1:], x[j]["val"]):
                            return True
                    return False
                else:
                    x = x[i]["val"]

    def addWord(self, word):
        self.insert(word)
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """

    def search(self, word):
        return self.searchDs(word, self.trieDs)
        # print("search",word)
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to             represent any one letter.
        :type word: str
        :rtype: bool
        """


