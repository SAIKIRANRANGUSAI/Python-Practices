
def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func()

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func()
    return inner


@star
@percent
def printer(msg):
    print(msg)

printer("Hello")