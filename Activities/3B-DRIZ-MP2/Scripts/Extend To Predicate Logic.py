def forall(predicate, domain):
    # It checks if the given predicate is true for every element in the domain
    return all(predicate(x) for x in domain)

def exists(predicate, domain):
    # It checks if there is at least one(1) element in the domain satisfies the predicate
    return any(predicate(x) for x in domain)
