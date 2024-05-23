               # dict

my_dict = {'Anna': 2001, 'Valentin': 1999, 'Demid': 2023}
print(my_dict)
print(my_dict.get('Anna'))
print(my_dict.get('Victoria'))
my_dict['Victoria'] = 2018
my_dict['Sasha'] = 2005
a = my_dict.pop('Demid')
print(a)
print(my_dict)

                #set

my_set = {1, 5.8, 5.8, 'Daria', 'a', 'a', 85.645, 85.645}
print(my_set)
my_set.add(89)
my_set.add(96.45)
my_set.discard(5.8)
print(my_set)
