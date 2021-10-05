# 'continue' example
def delete_spaces(sen):
    sen_no_spaces = ""
    for c in sen:
        if c.isspace():
            continue
        sen_no_spaces += c
    print(sen_no_spaces)


# TODO - change
delete_spaces("good moraning")