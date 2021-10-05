def play_fizzbuzz_v1(x):
    print("hi")


def test1():
    # Check for first value (because of the for loop)
    return play_fizzbuzz_v1(1) == [1]


def test2():
    # Sanity check, check for the second value of the for loop
    return play_fizzbuzz_v1(2) == [1, 2]


def test3():
    # Check for the first "Fizz" insertion
    return play_fizzbuzz_v1(3) == [1, 2, "Fizz"]


def test4():
    # Check for the first "Buzz" insertion
    return play_fizzbuzz_v1(5) == [1, 2, "Fizz", 4, "Buzz"]


def test5():
    # Check for the second "Buzz" insertion
    return play_fizzbuzz_v1(10) == [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz']


def test6():
    # Check for the first "FizzBuzz" insertion
    return play_fizzbuzz_v1(15) == [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14,
                                    'FizzBuzz']


def test7():
    # Check for the first insertion after the first "FizzBuzz" insertion
    return play_fizzbuzz_v1(16) == [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14,
                                    'FizzBuzz', 16]
