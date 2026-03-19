def login(username, password):
    # TODO: implement login logic
    if username == 'admin' and password == '123':
        return True
    return False

def logout(username):
    print(f'User {username} logged out')
