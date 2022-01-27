class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + self.age


d = Dog("yasser", "19 år gammal ")

print(d)
