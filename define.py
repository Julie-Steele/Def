#from my googling, it sadly seems you can't redefine "def". Here's the next best

def type_output(func, output_type):
    """type checks the output of func and errors if not output type"""
    def tfunc (*args):
        to_return = func(*args)
        if type(to_return) != output_type:
            raise TypeError("Function returned " + str(type(to_return)) + " Expected output type: " + str(output_type))
        
        return to_return 
    return tfunc

#EXAMPLE
def add(a: int, b: int) -> int:
    return a+b

print(add(1, 2))


add = type_output(add, int)
print(add(1, 2)) #same functionality because correct type


add_string = type_output(add, str)
print(add_string(1, 2)) #TypeError because not a string 





