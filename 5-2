def deco2_add(type):
    def decorator(func):
        def wrapper(a, b):
            result = func(a, b)
            if type == "math":
                return f"{a} + {b} = {result}"
            elif type == "word":
                return f"The sum of {a} and {b} is {result}"
            else:
                return result
        return wrapper
    return decorator

# 1. type="math" 테스트
@deco2_add(type="math")
def add_math(a, b):
    return a + b

print(add_math(2, 4))

# 2. type="word" 테스트
@deco2_add(type="word")
def add_word(a, b):
    return a + b

print(add_word(1, 2))
