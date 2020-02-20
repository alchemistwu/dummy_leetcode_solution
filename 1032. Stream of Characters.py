"""
Link: https://leetcode.com/problems/stream-of-characters/
"""
from typing import List

class Trie:
    def __init__(self):
        self.flag = False
        self.dict = {}


class StreamChecker:
    def __init__(self, words: List[str]):
        self.maxLengthWord = 0
        self.window = []
        self.root = self.createTree(words)


    def query(self, letter: str) -> bool:
        if len(self.window) == self.maxLengthWord:
            self.window.pop(0)
        self.window.append(letter)
        cur = self.root
        for letter in self.window[::-1]:
            if letter in cur.dict.keys():
                cur = cur.dict[letter]
                if cur.flag:
                    return True
            else:
                return False
        return cur.flag

    def createTree(self, words):
        root = Trie()
        for word in words:
            if len(word) > self.maxLengthWord:
                self.maxLengthWord = len(word)
            cur = root
            for character in word[::-1]:
                if character not in cur.dict.keys():
                    cur.dict[character] = Trie()
                cur = cur.dict[character]
            cur.flag = True
        return root

if __name__ == '__main__':
    obj = StreamChecker(["cd","f","kl"])
    test_stream = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    for letter in test_stream:
        print(obj.query(letter))
