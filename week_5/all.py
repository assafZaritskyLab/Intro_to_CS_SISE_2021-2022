
# Tip
def just_run_rec(n):
    if n == 0:
        return
    return just_run_rec(n - 1)


just_run_rec(100)
