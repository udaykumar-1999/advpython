def deco_with_args(a, b, c):
    def picker(func):
        def wrapper(*args):
            print("wrapper can access all variables\n"
                  "\t from decorator with args:{0} {1} {2}\n"
                  "\t from function call: {3}\n"
                  .format(a, b, c, args))
            return func(*args)

        return wrapper

    return picker


@deco_with_args("panda", "lion", "tiger")
def show(a, b, c):
    print("this is decorated fun with args {0},{1},{2}".format(a, b, c))


show("china", "africa", "india")


# -----------------------------------------

def decor2(func):
    def inner():
        x = func()
        print("x in decor 3rd..", x)
        return x + 100

    return inner


def decor1(func):
    def inner():
        x = func()
        print("x in decor 2nd..", x)
        return x * x

    return inner


def decor(func):
    def inner():
        x = func()
        print("x in decor 1st..", x)
        return 2 * x  # input for next decor func

    return inner


@decor2
@decor1
@decor
def num():
    return 10


num()
