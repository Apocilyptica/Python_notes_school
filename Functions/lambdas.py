full_name = lambda first, last: f'{first} {last}'

def greeting(name):
    print(f'Hi there {name}')


greeting(full_name('Tiffany', 'Hudgens'))