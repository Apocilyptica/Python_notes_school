username = 'jonsnow'
email = 'jon@snow.com'
password = 'thenorth'

username = input('Enter Email or username:\n')
email = username
password = input('Enter password:\n')
if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':
    logged_in = True
    standard_user = True
    print('Access permitted')
else:
    print('You shall not pass!')

if logged_in and not standard_user:
    print('You can access the admin dashboard')
else:
    print('You can only access the standard dashboard')

