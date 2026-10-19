class Cat:
    # TODO 1: add an extra parameter to the constructor to define the colour
    # of the cat and store it for use
    def __init__(self, name,color = ""):
        self.name = name
        self.color = color

    def meow(self):
        print(f"Meow  my name is {self.name}")

    # TODO 2: Define a method called Jump that takes in a value and prints
    # "The {color} cat jumps x meters high"
    # NOTE: the {color} part refers to the colour attribute you defined
    # in the constructor above.
    def jump(self,x):
        print(f'The {self.color} cat jumps {x} meters high')


def demo():
    cat1 = Cat("sussie")

    cat2 = Cat("Bob")

    # TODO 3: Create a new cat object with name JOHN and colour purple
    cat3 = Cat("JOHN","Purple")

    cat1.meow()
    cat2.meow()

    cat1.name = "Tiffany"

    # TODO 4: Change the colour of cat 2 to be white and observe the change
    cat2.color = "White"

    cat1.meow()
    cat2.meow()

    # TODO 5: Call the newly defined Jump method on each cat here
    # and observe what it prints
    cat1.jump(5)
    cat2.jump(5)
    cat3.jump(5)
    

    #TODO 5 Call the newly defined jump method on each cat here and observe what it prints


demo()
