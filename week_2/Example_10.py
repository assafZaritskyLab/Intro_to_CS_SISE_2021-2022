# 'break' example
def is_string_contain_num(is_number):
    for c in is_number:
        if c.isdigit():
            print("A number was found:", c)
            break
        else:
            print("Found '" + c + "' which is not a number!")
    print("done!")


is_string_contain_num("ab4cde")