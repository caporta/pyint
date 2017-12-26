def make_adder(x):
    def add(y):
        result = x + y
        print(result)
        return result
    return add

add_five = make_adder(5)
print(add_five.__closure__)
add_five(5)
