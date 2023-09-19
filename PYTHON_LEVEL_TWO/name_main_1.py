def func():
    print("func() in name_main_1.py")

print("TOP LEVEL NAME_MAIN_1.PY")

if __name__ == '__main__':
    #logic goes here
    print("name_main_1.py is being run directly")
else:
    print("name_main_1 has been imported")