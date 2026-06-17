class Circle():
    def __init__(self, radius):
        # initilizes self with radius
        self.radius = radius

    def get_radius(self):
        # returns radius of self
        pass

    def set_radius(self, radius):
        # changes the radius attribute of self to radius
        pass

    def area(self):
        # computes and returns area of self
        pass

    def __eq__(self, other):
        # other is a Circle object
        # returns True if self and other has the same radius value
        pass

    def __gt__(self, other):
        # other is a Circle object
        # returns self or other, Circle object with the bigger radius
        pass

    def __add__(self, other):
        # other is a Circle object
        # returns a new Circle object that it's radius is
        #  the sum of self and other's radius
        pass

    def __str__(self):
        # a Circle's string reperesentation is the radius
        pass
    