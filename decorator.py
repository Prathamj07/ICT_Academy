def dec(func):
    def wrapper(*a,**ka):
        print("Something")
        var = func(*a,**ka)
        return var
    return wrapper

@dec
def xyz():
    print("hello")