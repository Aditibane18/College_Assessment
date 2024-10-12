#Question 1
def suggest(search_history, partial_query):
    partial_query = partial_query.lower()
    suggestions = []
    for item in search_history:
        if item.lower().startswith(partial_query):
            suggestions.append(item)

    return suggestions

search_history = [
    "apple",
    "banana",
    "carrot",
    "pear",
    "pineapple",
    "potato",
    "strawberry"
]

partial_query = input("Enter your partial search query: ")
suggestions = suggest(search_history, partial_query)

if suggestions:
    print("Suggestions:")
    for suggestion in suggestions:
        print(suggestion)
else:
    print("No suggestions found.")



