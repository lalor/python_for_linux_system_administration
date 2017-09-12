def check_required_args(parameters):
    """check parameters of action"""
    def decorated(f):
        """decorator"""
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            """wrapper"""
            func_args = inspect.getcallargs(f, *args, **kwargs)
            for item in parameters:
                if func_args.get(item) is None:
                    message = "check required args failed, `{0}` is not found in {1}".format(item, f.__name__)
                    LOG.error(message)
                    raise Exception(message)

            return f(*args, **kwargs)
        return wrapper
    return decorated
