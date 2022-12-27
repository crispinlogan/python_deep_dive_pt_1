####
# From first part - up to and including 102 - Closures
####
"""
# show the example of closures accessing the free var (when a list so mem address is different -
# not an interened object like a short string) and also the issue (i.e. for loop thing)

def outer():
    x = [1,2,3]
    print(hex(id(x)))
    def inner():
        x = [1,2,3]
        print(hex(id(x)))
    return inner

# here you can see memory address is different for x and y lists
a = outer()
a() # this gives a different address when run line by line in terminal (as expected) but not when we run the entire script! odd! let's not worry about it for now...could be a difference with me using python 3.8/9 whereas Fred Baptiste is using 3.6
# print(a.__closure__) # not a closure!
# print(a.__code__.co_freevars) # not a closure!
"""

# now let's make a closure and you can see that the memory address
# is shared as x is now the free variable in the eextended scope that is required in the inner fn
def outer():
    x = [1,2,3]
    print(hex(id(x)))
    def inner():
        y = x
        print(hex(id(y)))
    return inner

# here you can see memory address is the same for x and y lists as they reference the same value
a = outer()
a()
print(a.__closure__) # not a closure!
print(a.__code__.co_freevars) # not a closure!

# now lets see a potential trap!
def adder(n):
    def inner(x):
        return x+n
    return inner

a = adder(5)
a(4)
a(1)

a1 = adder(1)
a2 = adder(2)
a3 = adder(3)

a1(4)
a2(4)
a3(4)

# but here is the trap - we might think we do the below - but actually this is not a closure,
# the n is the global variable and ends up being the final n in the for loop when we finish
# the loop and later call the adder fns
adders = []
for n in range(1,5):
    adders.append(lambda x: x+n)


adders[0](3)
adders[1](3)
adders[2](3)



# instead we still have to use the function adder to create the closure and reference the actual n we expect
adders = []
for n in range(1,5):
    adders.append(adder(n))


adders[0](3)
adders[1](3)
adders[2](3)
