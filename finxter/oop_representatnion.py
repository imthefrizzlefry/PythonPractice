class Person:
    def __init__(self, name, gender, height):
        self.name = name
        self.gender = gender
        self.height = height
    
    def __repr__(self):
        s = 'Tall ' * (self.height > 165)
        s += self.name
        return s
        

p = Person('Joe', 'Boy', 170)
q = Person('Mary', 'Girl', 160)
print([p, q])