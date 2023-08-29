# We can use these keywords:
    # Try
    # Except
    #Finally

# print('hello) # Will give syntax Error
# print(mylist) # Will through Name Error name mylist s not defined

# try:
#     f = open('simple.txt','w')
#     f.write("Test write to simple text!")
# except IOError:
#     print("ERROR: COULD NOT FIND OR READ DATA!")
# else:
#     print("SUCCESS!")
#     f.close()
# print("hello world!")

# Similar example with the finally block
try:
    f = open('simple.txt','r')
    f.write("Test write to simple text!")
except IOError:
    print("ERROR: COULD NOT FIND OR READ DATA!")
finally:
    print("I always work no matter what!")