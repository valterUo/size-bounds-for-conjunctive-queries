def shannon_inequalities(variables):
    fds = []
    for i in variables:
        fds.append([[x for x in variables if x != i], i])
    return fds