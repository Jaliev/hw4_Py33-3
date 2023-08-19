class A:
    def __init__(self, name):
        self.name = name
class B:
    def __init__(self, age):
        self.age = age
class C:
    def __len__(self):
        return len(self.name)
class D:
    def __str__(self):
        return f'Age: {self.age}'

ars = A('Arslanbek')
ars2 = B(28)

# print('Name:', ars.name)
# print('Len name:', C.__len__(ars))
# print(D.__str__(ars2))
