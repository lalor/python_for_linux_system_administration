def check_is_admin(username):
    if username != 'admin':
        raise Exception("This user is not allowed to put/get elem")

class Stack:
    def __init__(self):
        self.storage = []

    def put(self, username, elem):
        check_is_admin(username=username)
        self.storage.append(elem)

    def get(self, username):
        check_is_admin(username=username)
        if not self.storage:
            raise Exception("There is no elem in stack")
        return self.storage.pop()
