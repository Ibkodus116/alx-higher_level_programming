def safe_print_division(a, b):
    num = 0
    try:
        num = a / b
    except ZeroDivisionError:
        num = None
        return None
    else:
        return num
    finally:
        print("Inside result: {}".format(num))
