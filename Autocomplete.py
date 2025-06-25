def autocomplete(self, prefix, top_n =3):
    node = self.root
    for char in prefix:
        if char not in node.children:
            print(f"No suggestions for prefix '{prefix}'")
            return []

        node = node.children[char]

    #Now at the node for the given prefix
    result =heap[]


def dfs(current_node):
    if current_node.is_end_of_word:
        #Use -freq to simulate max heap
        heapq.heappush(result_heap,(-current_node.frequency, current_node.word))
    for child in current_node.children.value():
        dfs(child)

dfs(node)

#Get top_n words by frequency
top_suggestions=[]
for _ in range(min(top_n,len(result_heap))):
    freq, word = heapq.heappop(result_heap)
    top_suggestions.append((word,-freq))

return top_suggestions