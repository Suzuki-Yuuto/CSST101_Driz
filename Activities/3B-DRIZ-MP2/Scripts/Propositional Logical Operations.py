def and_operation(p,q):
    # it will return as true if both variables are true
    return p and q

def or_operation(p,q):
    # if either variable is true then it will return as true
    return p or q

def not_operation(p):
    # if the variable is true then it will return as false and vice versa
    return not p

def implies_operation(p,q):
    # it will only return as false if 'p' is true and 'q' is false
    return not p or q