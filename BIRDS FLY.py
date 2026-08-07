# Birds Fly Knowledge Base

birds = ["sparrow", "eagle", "parrot", "penguin", "ostrich"]

cannot_fly = ["penguin", "ostrich"]

def can_fly(animal):

    if animal in birds:

        if animal in cannot_fly:
            return animal + " cannot fly"

        else:
            return animal + " can fly"

    else:
        return animal + " is not a bird"


print(can_fly("sparrow"))
print(can_fly("eagle"))
print(can_fly("penguin"))
print(can_fly("ostrich"))