class System:

    def __init__(self):
        self.online_users = []

    def register(self, name, password):
        try:
            f = open('ps_8_files/users.txt', 'r')
        except:
            print("Congrats! You are the first user!")
        else:
            for line in f:
                if name == line.strip().split()[0]:   # strip = Remove spaces at the beginning and at the end of the string:
                    f.close()
                    raise ValueError(name + " is taken, choose different one")
            f.close()
        f = open('ps_8_files/users.txt', 'a')
        f.write(name + " " + password + "\n")
        f.close()
        print(name + ' has been registered!')

    def login(self, name, password):
        if name in self.online_users:
            print(name + ' is already logged in!')
            return
        try:
            f = open('ps_8_files/users.txt', 'r')
        except:
            print("No registered users yet!")
            return
        else:
            for line in f:
                line = line.strip().split()
                if name == line[0] and password == line[1]:
                    self.online_users.append(name)
                    print(name + ' has logged in!')
                    f.close()  # todo close
                    return
            f.close()  # todo close
        print("Wrong username or password!")


# Create new System
s = System()
s.register('Hanna', '123123')
s.register('Amir', '456456')
try:
    s.register('Hanna', '789789')
except Exception as e:
    print(e)

s.register('Bob', '111222')
s.register('Alice', '333444')
# Login in examples


s = System()
s.login('Hanna', '123123')
s.login('Amir', '456456')
try:
    s.login('Bob', 'wrong_pass')
except Exception as e:
    print(e)
s.login('Hanna', '123123')

print(s.online_users)



