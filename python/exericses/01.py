# The below program gives error why ?

'''
def foo(a, b):
    print(a + b)

x = foo(2, 3) * 10
print(x)
'''


'''
TypeError because Python cannot multiply a None type object with an integer.
The function output is what produces a None object because the function definition is not returning anything.
Fix it by using return  instead of print :
'''


def foo(a, b):
    return a + b


x = foo(2, 3) * 10
print(x)
