def decorator_question(function):
    def wrapper(*args, **kwargs):
        print(''.join(['*' for _ in range(100)]))
        print('\n*********************************** Question ********************************\n')
        function(*args, **kwargs)
        print(''.join(['*' for _ in range(100)]))

    return wrapper
