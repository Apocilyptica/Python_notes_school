def full_name(first, last):
    print(f'{first} {last}')


full_name('James', 'Jager')

def auth(email, password):
    if email == 'kristine@hudgens.com' and password == 'secret':
        print('Authorized')
    else:
        print('Not Authorized')


auth('jordan@hudgens.com', 'secret')
auth('kristine@hudgens.com', 'secret')

def counter(max_value):
    for num in range(1, max_value):
        print(num)


counter(501)