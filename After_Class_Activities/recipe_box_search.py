# RECIPE BOX SEARCH
# ---------- SETUP (given to you) ----------
RECIPES = [
    ("Pancakes", "mix flour eggs and milk then fry the batter in a pan"),
    ("Tomato Soup", "cook tomatoes with onion and salt then blend the soup"),
    ("Fruit Salad", "chop apple banana and mango and mix the fruit in a bowl"),
    ("Omelette", "beat eggs with salt and cook the eggs in a pan"),
    ("Cookies", "mix flour butter and sugar then bake the cookies"),
]

TEST_SEARCHES = [
    ("fry the batter", "Pancakes"),
    ("blend the soup", "Tomato Soup"),
    ("mango and apple", "Fruit Salad"),
    ("eggs in a pan", "Omelette"),
    ("butter and sugar", "Cookies"),
    ("cookie", "Cookies"),
]

# ---------- PART 1: build the index ----------
def build_index(recipes):
    index = {}
    # YOUR CODE HERE
    # For each (number, (title, text)) from enumerate(recipes), and for each word of text.split():
    # add 1 to index[word][number]. Make index[word] an empty dictionary the first time you see the word.
    return index

INDEX = build_index(RECIPES)
print("PART 1: Index")
print(INDEX.get("eggs"), INDEX.get("pizza", "not found"))

# ---------- PART 2: score the recipes ----------
def score(query):
    scores = {}
    # YOUR CODE HERE
    # For each word of query.split(), and each (number, count) in INDEX.get(word, {}).items():
    # add count divided by the number of words in that recipe's text to scores[number].
    return scores

print("\nPART 2: Score")
print(round(score("eggs in a pan").get(3, 0), 2))

# ---------- PART 3: find the best recipe ----------
def best_recipe(query):
    # YOUR CODE HERE
    # Get the scores. If there are none, return "no match".
    # Otherwise return the title of the recipe with the highest score.
    return "no match"

print("\nPART 3: Best recipe")
print(best_recipe("fry the batter"), "|", best_recipe("pizza"))

# ---------- PART 4: check every test search ----------
print("\nPART 4: Test all searches")
mistakes = 0
# YOUR CODE HERE
# For each (query, wanted) pair: get the answer from best_recipe, add 1 to mistakes
# if it is not the wanted one, and print the answer and the query on one line.
# After the loop, print: Mistakes: <number> out of <total>
