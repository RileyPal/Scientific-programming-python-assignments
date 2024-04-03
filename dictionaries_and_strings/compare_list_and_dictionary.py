code_snippets = {
    "numbers": '''numbers = {}
numbers[0] = -5
numbers[1] = 10.5''',

    "other_numbers": '''other_numbers = []
other_numbers[0] = -5
other_numbers[1] = 10.5''',
}

explanations = {
    "numbers": "Assigning values to keys of a dictionary.",
    "other_numbers": "Attempting to assign values to indices of a list, which raises an IndexError.",
}

fixed_snippets = {
    "other_numbers": '''other_numbers = []
other_numbers.append(-5)
other_numbers.append(10.5)'''
}

for snippet_name, snippet_code in code_snippets.items():
    print("Code snippet:")
    print(snippet_code)
    print("Explanation:")
    print(explanations[snippet_name])
    print("Fixed snippet:" if snippet_name in fixed_snippets else "--------------")
    print(fixed_snippets.get(snippet_name, "No fix needed"))
    print("\n")