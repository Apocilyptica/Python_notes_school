def greeting(name = 'Guest'):
  print(f'Hi {name}!')

greeting()
greeting('Kristine')

# Interview problem very bad practice to set a default as a list
def some_function(collection = []):
    collection.append(1)
    print(id(collection))
    return collection

print(some_function()) # [1]

# Other part of program
print(some_function()) # [1, 1]