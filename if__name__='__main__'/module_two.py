import module_one

print(__name__)
print(module_one.__name__)

#when we run from module two, it will say running other module indirectly

#In order to use the function hello() from module one, we need to import the module then:

#module_one.hello()