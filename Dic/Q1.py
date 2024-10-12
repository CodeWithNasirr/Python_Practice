# Q what is distctory compressions in python
# {key_expression: value_expression for item in iterable if condition}
# In Python, dictionary comprehension is a concise way to create dictionaries from iterables by transforming or filtering the items. It works similarly to list comprehension, but instead of creating lists, it generates dictionaries with key-value pairs.


# How do you invert a dictionary (swap keys and values)?
my_dict = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = {k:v for v,k in my_dict.items()}
print(inverted_dict)