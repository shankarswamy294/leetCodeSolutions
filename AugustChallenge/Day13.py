# Design an Iterator class, which has:
#
# A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
# A function next() that returns the next combination of length combinationLength in lexicographical order.
# A function hasNext() that returns True if and only if there exists a next combination.

# Example:
#
# CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.
#
# iterator.next(); // returns "ab"
# iterator.hasNext(); // returns true
# iterator.next(); // returns "ac"
# iterator.hasNext(); // returns true
# iterator.next(); // returns "bc"
# iterator.hasNext(); // returns false

class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        self.characters = characters
        self.combinationLength = combinationLength
        self.combinations = []
        self.generate_comb()
        self.currert_comb = len(self.combinations) - 1

    def get_str(self, bin_str):
        ans = ""
        for index, b in enumerate(bin_str):
            ans = ans + self.characters[index] if b == "1" else ans
        return ans

    def generate_comb(self):
        l = len(self.characters)
        bin_len = int('1' * l, 2)
        for a in range(bin_len + 1):
            temp = bin(a)[2:].rjust(l, "0")
            self.combinations.append(temp) if temp.count("1") == self.combinationLength else None

    def next(self):
        ans = self.get_str(self.combinations[self.currert_comb])
        self.currert_comb -= 1
        return ans

    def hasNext(self):
        return self.currert_comb >= 0
