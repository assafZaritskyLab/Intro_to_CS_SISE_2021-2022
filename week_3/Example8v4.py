def play_fizzbuzz_v4(x):
    ans = []
    for num in range(1, x+1):
        if num % 3 == 0:
            ans.append('Fizz')
        elif num % 5 == 0:
            ans.append('Buzz')
        elif num % 3 == 0 and num % 5 == 0:
            ans.append('FizzBuzz')
        else:
            ans.append(num)
    return ans

def test1():
    # Check for first value (because of the for loop)
    return play_fizzbuzz_v4(1) == [1]
def test2():
    # Sanity check, check for the second value of the for loop
    return play_fizzbuzz_v4(2) == [1,2]
def test3():
    # Check for the first "Fizz" insertion
    return play_fizzbuzz_v4(3) == [1,2,"Fizz"]
def test4():
    # Check for the first "Buzz" insertion
    return play_fizzbuzz_v4(5) == [1,2,"Fizz",4,"Buzz"]
def test5():
    # Check for the second "Buzz" insertion
    return play_fizzbuzz_v4(10) == [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz']
def test6():
    # Check for the first "FizzBuzz" insertion
    return play_fizzbuzz_v4(15) == [1,2,'Fizz',4,'Buzz','Fizz',7,8,'Fizz','Buzz',11,'Fizz',13,14,'FizzBuzz']
def test7():
    # Check for the first insertion after the first "FizzBuzz" insertion
    return play_fizzbuzz_v4(16) == [1,2,'Fizz',4,'Buzz','Fizz',7,8,'Fizz','Buzz',11,'Fizz',13,14,'FizzBuzz',16]

print("Test 1:", test1())
print("Test 2:", test2())
print("Test 3:", test3())
print("Test 4:", test4())
print("Test 5:", test5())
print("Test 6:", test6())
print("Test 7:", test7())