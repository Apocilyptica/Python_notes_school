api_data = '5'
greeting = 'Hi'

#print(api_data.isalpha())
#print(greeting.isalpha())

print(api_data.isnumeric())
print(greeting.isnumeric())

# The space is not alphanumeric so you get a false
greeting = 'Hi there'

print(greeting.isalpha())