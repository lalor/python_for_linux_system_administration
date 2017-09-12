def check_is_admin(f):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception("This user is not allowed to put/get elem")
        return f(*args, **kwargs)
    return wrapper


class Stack:
    def __init__(self):
        self.storage = []

    @check_is_admin
    def put(self, username, elem):
        self.storage.append(elem)

    @check_is_admin
    def get(self, username):
        if not self.storage:
            raise Exception("There is no elem in stack")
        return self.storage.pop()
