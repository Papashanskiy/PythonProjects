

def decorator_func(fn):
    def wrapper(arg1, arg2):
        print('look what I have:', arg1, arg2)
        fn(arg1, arg2)
    return wrapper


@decorator_func
def print_full_name(first_name, last_name):
    print("Меня зовут", first_name, last_name)


print_full_name('dima', 'apashanskiy')
