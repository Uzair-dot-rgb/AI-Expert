# NEXT WORD NOTEBOOK
# ---------- SETUP (given to you) ----------
TEXT = "the cat sat on the mat and the cat ate the fish and the dog sat on the rug"
WORDS = TEXT.split()

TEST_WORDS = [
    ("the", "cat"),
    ("sat", "on"),
    ("and", "the"),
    ("dog", "sat"),
    ("pizza", "the"),
    ("cat", "ate"),
]

# ---------- PART 1: count what follows what ----------
def build_bigrams(words):
    model = {}
    # YOUR CODE HERE
    # For each pair from zip(words, words[1:]), add 1 to model[current][following].
    # The first time you see current, give it an empty dictionary. Use .get(following, 0) + 1 for the count.
    return model

BIGRAMS = build_bigrams(WORDS)
print("PART 1: Bigrams")
print(BIGRAMS.get("the"), BIGRAMS.get("pizza", "not found"))

# ---------- PART 2: turn counts into probabilities ----------
def probabilities(word):
    result = {}
    # YOUR CODE HERE
    # counts = BIGRAMS.get(word, {}) gives what followed the word ({} if it was never seen).
    # For each following word and count, store count divided by the sum of all the counts in result.
    return result

print("\nPART 2: Probabilities")
print({w: round(p, 2) for w, p in probabilities("the").items()})

# ---------- PART 3: predict the next word ----------
def predict(word):
    # YOUR CODE HERE
    # Get the probabilities of the word. If there are none, return "the" (the most common word in the text).
    # Otherwise return the following word with the highest probability: max(chances, key=chances.get)
    return "the"

print("\nPART 3: Predict")
print(predict("the"), "|", predict("pizza"))

# ---------- PART 4: check every test word ----------
print("\nPART 4: Test all words")
mistakes = 0
# YOUR CODE HERE
# For each (word, wanted) pair: get the answer from predict, add 1 to mistakes
# if it is not the wanted one, and print the word and the answer on one line.
# After the loop, print: Mistakes: <number> out of <total>
