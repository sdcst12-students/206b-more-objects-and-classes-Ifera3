#!python3

class quadratic:
    a = 0
    b = 0
    c = 0
    roots = []

    def discriminant(self):
        # requires no positional arguments
        # will make use of class properties a,b and c 
        # to determine the discriminant which is calculated as 
        # b^2 - 4ac
        # return value should be a float type decimal
        discr = (self.b**2) - (4*self.a*self.c)
        return discr
    
    def hasRealRoots(self):
        # requires no positional arguments
        # will make use of class properties a,b and c 
        # to determine if the quadratic has real roots
        # defined when the discriminant is non negative
        # return value should be True or False
        if self.discriminant() < 0:
            return False
        else:
            #self.calcRoots()
            return True

    def isFactorable(self):
        # requires no positional arguments
        # will make use of class properties a,b and c 
        # to determine if the quadratic can be factored
        # quadratic can be factored if the discriminant is a perfect square
        # return value is True or False
        discr = self.discriminant()
        #print(discr)
        if self.hasRealRoots():
            if (discr**0.5) % 2 == 0 or (discr**0.5) % 2 == 1:
                return True
        return False
    
    def calcRoots(self):
        # requires no positional arguments
        # will make use of class properties a,b and c 
        # to determine the roots of the quadratic if
        # the quadratic has real roots
        # should make use of the class methods:
        # self.hasRealRoots()
        # self.discriminant()
        # method does not have a return value
        # but should store the values of the roots in the 
        # list self.roots
        # list should be sorted in ascending order
        # roots should be rounded to 2 decimal places
        if self.hasRealRoots():
            tempRoot1 = (-self.b - (self.discriminant()**0.5)) / (2*self.a)
            tempRoot2 = (-self.b + (self.discriminant()**0.5)) / (2*self.a)
            self.roots = [round(tempRoot1,2), round(tempRoot2,2)]
            self.roots.sort()
        #print(self.roots)

    def axisOfSymmetry(self):
        # requires no positional arguments
        # will make use of class properties a,b and c 
        # to determine the x value that is for the equation
        # of the axis of symmetry
        # should return the x value for the axis of symmetry
        aos = -self.b / (2*self.a)
        #print(aos)
        return round(aos,2)

    def vertex(self):
        # requires no positional arguments
        # will make use of class properties a,b and c 
        # to determine the x,y value of the vertex
        # should return the a list with the x and y coordinates of the vertex
        x = self.axisOfSymmetry()
        y = (self.a * (x**2)) + (self.b * x) + self.c
        return [x, y]
        
    def __init__(self, ax2, bx, cons):
        # this should require 3 positional arguments and assign the values
        # to self.a, self.b and self.c
        try:
            self.a = int(ax2)
            self.b = int(bx)
            self.c = int(cons)
        except:
            print("invalide entres")


if __name__ == "__main__":
    q1 = quadratic(1,4,4)
    assert q1.isFactorable() == True
    assert q1.hasRealRoots() == True
    assert q1.discriminant() == 0
    q1.calcRoots()
    assert q1.roots == [-2,-2]
    assert q1.axisOfSymmetry() == -2
    assert q1.vertex() == [-2,0]

    q2 = quadratic(1,1,-6)
    assert q2.isFactorable() == True
    assert q2.hasRealRoots() == True
    assert q2.discriminant() == 25
    q2.calcRoots()
    assert q2.roots == [-3,2]
    assert q2.axisOfSymmetry() == -0.5
    assert q2.vertex() == [-0.5,-6.25]

    q3 = quadratic(1,1,10)
    assert q3.isFactorable() == False
    assert q3.hasRealRoots() == False
    assert q3.discriminant() == -39
    q3.calcRoots()
    assert q3.roots == []
    assert q3.axisOfSymmetry() == -0.5

    q4 = quadratic(1,10,1)
    assert q4.isFactorable() == False
    assert q4.hasRealRoots() == True
    assert q4.discriminant() == 96
    q4.calcRoots()
    assert q4.roots == [-9.90,-0.10]
    assert q4.axisOfSymmetry() == -5 # was -2.5 but after checking myself it was -5. fixed assret to include real axis of symmetry
