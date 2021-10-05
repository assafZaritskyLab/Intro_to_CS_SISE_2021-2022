
### Question 3 - Pangrams
def is_pangram(s):
    d = {}
    for char in s:
        if char.isalpha():
            d[char.lower()] = True
    return (len(d.keys()) == 26)


s = " The quick brown fox jumps over the lazy dog"
print(is_pangram(s))
s = " The quick fox jumps over the lazy dog"
print(is_pangram(s))
