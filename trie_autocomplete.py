from collections import defaultdict
import heapq

class TrieNode:
    def  __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end_of_word = False
        self.frequency = 0
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word, frequency =1):
        node = self.root
        for char in word:
            node = node.children[char]
        node.is_end_of_word =True
        node.frequency +=frequency
        node.word = word 