import homework4
from homework4 import A, B, C, D
class E(A, B, C, D):
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age

homework4.ars2.__age = 'hidden'

print('Name:', homework4.ars.name)
print('Age:', homework4.ars2.__age)

# вывод истинного возраста:
# print('Age:', homework4.ars2.age)