import functools


def markdown2html(cssfiles=None):
    def decorator(handler):
        @functools.wraps(handler)
        def wrapper(*args, **kwargs):
            return handler(*args, **kwargs)

        return wrapper

    return decorator
