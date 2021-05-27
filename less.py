def fn():
    count = 0

    def function():
        nonlocal count
        count += 1
        print(count)
    return function


# a = fn()
# a()
# a()
# a()
fn()()
fn()()
fn()()



