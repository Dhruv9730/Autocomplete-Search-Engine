# 🔍 Autocomplete Search Engine – Typo-Tolerant & Self-Learning (DSA + NLP)

This is an intelligent **Autocomplete Search Engine** inspired by how Google, IntelliSense, and e-commerce platforms build real-time search features.

Built entirely in **Python** using:
- ✅ Trie (prefix tree) for fast lookup
- ✅ Heap for ranking top-N suggestions
- ✅ Levenshtein Distance for typo correction
- ✅ Auto-Learning: frequency increases when a word is used
- ✅ Optional fuzzy match fallback if no prefix match is found

---

## 🧠 Key Features

| Feature                            | Tech / DSA Used              |
|-----------------------------------|------------------------------|
| Autocomplete by prefix            | Trie + Heap                  |
| Ranking by usage frequency        | Max Heap (based on counts)   |
| Auto-learning from user selection | In-place frequency updates   |
| Typo-tolerant search              | Levenshtein distance         |
| Spelling correction               | Fuzzy prefix + correction    |

🔁 Example Usage

trie.insert("help", 8)
trie.insert("helper", 5)
trie.insert("hello", 6)

# Smart autocomplete
smart_autocomplete(trie, "hel")
>> [('help', 8), ('helper', 5), ('hello', 6)]

# Typo handling
smart_autocomplete(trie, "hepl")
>> [('help', 8), ('helper', 5)]

# Auto-learn when word is selected
trie.increase_frequency("helper")
smart_autocomplete(trie, "hel")
>> [('helper', 6), ('help', 8)]

