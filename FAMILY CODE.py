# Family Knowledge Base

parent = {
    "John": ["Alice", "Bob"],
    "Alice": ["Charlie"],
    "Bob": ["David"]
}

gender = {
    "John": "male",
    "Alice": "female",
    "Bob": "male",
    "Charlie": "male",
    "David": "male"
}

def find_relationship(x, y):

    # Parent
    if y in parent.get(x, []):
        if gender.get(x) == "male":
            return x + " is the father of " + y
        else:
            return x + " is the mother of " + y

    # Grandparent
    for child in parent.get(x, []):
        if y in parent.get(child, []):
            return x + " is the grandparent of " + y

    # Sibling
    for p in parent:
        children = parent[p]
        if x in children and y in children and x != y:
            return x + " and " + y + " are siblings"

    return "Relationship not found"


print(find_relationship("John", "Charlie"))
print(find_relationship("Alice", "Bob"))