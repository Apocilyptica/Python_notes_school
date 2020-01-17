tags = ['python', 'development', 'tutorials', 'code']

# Nope
tags[-1] = 'Programming'
print(tags)

tags.extend('Programming')
tags.extend(['Programming'])
print(tags)

# Yup
new_tags = tags + ['Programmin']
print(new_tags)
print(tags)