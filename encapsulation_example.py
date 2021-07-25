'''
Encapsulation Example
private and Protected members
'''


class Modifiers:

    def __init__(self, name):
        self.__private_member = name
        self._protected_member = name


m = Modifiers('SKAUL05')
print(m.__private_member)  # we can't access Private members outside class or
# into subclass
# we can access only with format object._className.__private_member_name
print(m._Modifiers__private_member)
m._Modifiers__private_member = "Github"
print(m._Modifiers__private_member)

# protected member can be access outside class and can be modified too

print(m._protected_member)
m._protected_member = "Github"  # Changing Protected Attribute values
print(m._protected_member)
