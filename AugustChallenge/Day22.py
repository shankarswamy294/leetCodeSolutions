# Implement
# the
# StreamChecker
#
#
# class as follows:
#
#
# StreamChecker(words): Constructor, init
# the
# data
# structure
# with the given words.
# query(letter): returns
# true if and only if
# for some k >= 1, the last k characters queried ( in order from oldest to newest, including this letter just queried) spell one of the words in the given list.
#
# Example:
#
# StreamChecker
# streamChecker = new
# StreamChecker(["cd", "f", "kl"]); // init
# the
# dictionary.
# streamChecker.query('a'); // return false
# streamChecker.query('b'); // return false
# streamChecker.query('c'); // return false
# streamChecker.query('d'); // return true, because
# 'cd' is in the
# wordlist
# streamChecker.query('e'); // return false
# streamChecker.query('f'); // return true, because
# 'f' is in the
# wordlist
# streamChecker.query('g'); // return false
# streamChecker.query('h'); // return false
# streamChecker.query('i'); // return false
# streamChecker.query('j'); // return false
# streamChecker.query('k'); // return false
# streamChecker.query('l'); // return true, because
# 'kl' is in the
# wordlist

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.searchWord = ''
        for word in words:
            word = word[::-1]
            self.insertToTrie(self.trie, word)

    def insertToTrie(self, trie, word):
        if word[0] not in trie:
            trie[word[0]] = {"value": {}, "isLast": len(word) == 1}
        if len(word) == 1:
            trie[word[0]]["isLast"] = True
            return
        self.insertToTrie(trie[word[0]]["value"], word[1:])

    def searchForWord(self, trie, word):
        if not word or word[0] not in trie:
            return False
        if trie[word[0]]["isLast"]:
            return True
        return self.searchForWord(trie[word[0]]["value"], word[1:])

    def query(self, letter: str) -> bool:
        self.searchWord = letter + self.searchWord
        result = self.searchForWord(self.trie, self.searchWord)
        return result
