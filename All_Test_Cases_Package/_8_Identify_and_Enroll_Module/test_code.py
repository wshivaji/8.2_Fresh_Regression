
class MyClass:
    def __init__(self):
        pass

# Creating an instance of MyClass
obj = MyClass()

# Adding variables dynamically
setattr(obj, 'var1', 'value1')
setattr(obj, 'var2', 'value2')

# Printing the variables
print(obj.var1)
print(obj.var2)

# Appending variables dynamically
setattr(obj, 'var3', 'value3')

# Printing the appended variable
print(obj.var3)
