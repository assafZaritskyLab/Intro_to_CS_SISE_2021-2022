#
# This is a file!
# line 1.
# line 2.
# last line.

# this is an existing file


### Read mode
def read():
    f = open('ps_8_files/read.txt', 'r+')
    content = f.read()  # reads the whole file
    print(content)
    print('===============')
    f.write('this is a new line\n')
    f.seek(0)  # reset the line index
    print(f.readline())  # reads one line
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())  # Nothing will be printed here (end of file)
    f.close()
    #  print(f.readline().rstrip('\n')) - remove /n


# read()


def write():
    f = open('ps_8_files/write.txt', 'w+')
    # todo this will open the file and clear its content
    # a new file will be created if it doesn't exists
    f.write('We have created a new file!\n')
    print(f.readline())

    f.write('this is a new line\n')
    f.write('this is the last line')
    f.close()  # todo close the file after finish writing to save the content
    f = open('ps_8_files/write.txt', 'r')
    content = f.read()
    print(content)


write()


def append():
    f = open('ps_8_files/append.txt', 'a')
    f.write('\n')  # todo why
    f.write('append line 1\n')
    f.write('append line 2')
    f.close()
    f = open('ps_8_files/append.txt', 'r')
    content = f.read()
    print(content)


# append()


def example_1():
    try:
        f = open('ps_8_files/no_file.txt', 'r')
    except:
        print("The file doesn't exists")


# example_1()


def example_2():
    try:
        f = open('ps_8_files/read.txt', 'r')
        f.close()
        print(f.readline())
    except:
        print("The file is closed!")


example_2()

# def example_3():
#
#         f = open('ps_8_files/read.txt', 'r')
#         f1 = open('ps_8_files/read.txt', 'r')
#         print(f.readline())
#         print(f1.readline())
#         f.close()
#         f1.close()
#
# # example_3()
#
#
# def example_4():
#     f = open('ps_8_files/read.txt', 'w')
#     f1 = open('ps_8_files/read.txt', 'w')
#     f.write('append line 1\n')
#     f1.write('append line 2\n')
#     f.close()
#     f1.close()
#
#
# # example_4()
