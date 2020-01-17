post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

# Need to add a , to a tuple so that python dont think its math
# post = post + ('published',)
print(id(post))

post += ('published',)

title, sub_heading, content, status = post

print(title)
print(sub_heading)
print(content)
print(status)

print(id(post))