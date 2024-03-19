class Animals:
    breathe = True
    name = "Animal"
    can_jump = False

    def walk(self):
        print("I am walking")

    def jump(self):
        if self.can_jump:
            print("I am jumping")
        else:
            print("I am not jumping")


dog = Animals()
dog.name = 'Sobaka'

cat = Animals()
cat.name = "Koshka"

print(dog.name)
dog.walk()
dog.jump()

print(cat.name)
cat.walk()
cat.can_jump = True
cat.jump()


a = "asd"

print(a.upper())
