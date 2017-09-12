import functools
import inspect

def check_is_admin(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_args = inspect.getcallargs(func, *args, **kwargs)
        if func_args.get('username') != 'admin':
            raise Exception("This user is not allowed to put/get elem")
        return f(*args, **kwargs)
    return wrapper
