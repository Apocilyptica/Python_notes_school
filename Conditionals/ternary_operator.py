role = 'admin'

auth = 'can access' if role == 'admin' else 'cannot access'
print(auth)

role = 'guest'

auth = 'can access' if role == 'admin' else 'cannot access'
print(auth)