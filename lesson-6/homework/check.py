def check(func):
    def wrapper(*args):
        try:
            print(func(*args))
        except ZeroDivisionError:
            print("Denominator can't be zero")
    return wrapper

   


@check
def div(a, b):
   return a / b
div(6,0)