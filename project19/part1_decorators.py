

def bold(fn):
    def wrapped():
        return '<b>' + fn() + '</b>'
    return wrapped


@bold
def hello():
    return 'Hello world!'


new_hello = hello


print(new_hello())
