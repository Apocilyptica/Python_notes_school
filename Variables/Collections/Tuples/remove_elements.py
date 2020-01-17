post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

# Removing elements from end
post_one = post[:-1]
print(post_one)

# Removing elements from beginning
post_two = post[1:]
print(post_two)

# Removing specific element (messy/not recommended)
post_three = list(post)
post_three.remove('Intro guide to Python')
post_three = tuple(post_three)

print(post_three)