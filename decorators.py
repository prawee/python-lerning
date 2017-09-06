import functools

def my_decorators(func): 
    @functools.wraps(func)
    def function_that_runs_func():
        print("In the decorator!")
        func()
        print("After the decorator!")
    return function_that_runs_func

@my_decorators
def my_function():
    print("I'm the function!")

my_function()