def function_0():
    raise Exception("Exception has occurred!")
    print("function_0")


def function_1():
    function_0()
    print("function_1")


try:
    function_1()
except Exception as e:  # todo explain as e
    print(e)
else:
    print("shir here")
print("shir")



# todo example 1