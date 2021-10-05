# region question 1 - Which can be used as dictionary keys?

# dic_key_list = {[1, 2, 3]: 0} # TypeError: unhashable type: 'list'
# dic_key_dic = {{'1': 2}: 0} # TypeError: unhashable type: 'dict'
dic_key_tuple = {(1, 2): 0}
dic_key_string = {"1": 0}
dic_key_bool = {True: 0}
dic_key_float = {0.2: 0}
dic_key_int = {1: 0}
# dic_key_set = {{"apple", "banana", "cherry"}: 0} # TypeError: unhashable type: 'set'
# endregion

# region question 2 - Tuples, which is true
"""
    tuples content can be altered after initial creation. -> X 
    immutable
 
"""
"""
    you can't iterate over a tuple. -> X
    for i in (1, 2, 3):
        print(i)
"""
"""
    a tuple has no defined length => len(some_tuple) = None -> X
    tuple = (1, 2, 3)
    print(len(tuple)) # 3
 """
"""
    All of the above -> X
"""
"""
    None of the above-> V
"""
# endregion

# region  Question 3 - All recursive solutions can be written as iterative solutions:
# TRUE -> False
# False, but the opposite is true -> True
# False, and the opposite is False as well -> False
# endregion

# region Quesion 4 - and …
# think, therefore I am.
# need a coffee break?
# Feel great! Let's move on.
# Am confused. Let's reiterate.





