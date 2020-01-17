"""
remove_first_and_last(list_to_clean)

html = ['<h1>', 'Some content', '</h1>']

remove_first_and_last(html)
=> ['some content']

html_2 = ['<h1>', 'Some content', 'more', '</h1>']

remove_first_and_last(html_2)
=> ['some content', 'more']
"""

# My Solution
html = ['<h1>', 'Some content', '</h1>']
html_2 = ['<h1>', 'Some content', 'more', '</h1>']

def remove_first_and_last(list_to_clean):
    del list_to_clean[0]
    del list_to_clean[-1]
    return list_to_clean

print(remove_first_and_last(html))
print(remove_first_and_last(html_2))

# JH Solution
html = ['<h1>', 'Some content', '</h1>']
html_2 = ['<h1>', '</h1>']

# Glob up middle elements(destructering) one, *two, three = [1, 2, 3, 45, 6]

def remove_first_and_last(list_to_clean):
    if len(list_to_clean) > 2:
        _, *content, _ = list_to_clean
        return content
    else:
        return "Not enough content to clean"

print(remove_first_and_last(html))
print(remove_first_and_last(html_2))