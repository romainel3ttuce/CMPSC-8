# Handout 11:

# Question 1:

name_to_binomial = {'human': 'Homo sapiens',
                    'dog': 'Canis familiaris',
                    'narwhal': 'Monodon monoceros'}

print('dog' in name_to_binomial)
print('Canis familiaris' in name_to_binomial)
print(name_to_binomial == {'dog': 'Canis familiaris',
                           'narwhal': 'Monodon monoceros',
                           'human': 'Homo sapiens'})
print(len(name_to_binomial) == 3)
# print(name_to_binomial[0] == 'human')

# Question 2:

animal_to_locomotion = {'fish': ['swim'],
                        'kangaroo': ['hop'],
                        'frog': ['swim', 'hop']}

animal_to_locomotion['human'] = ['swim', 'run', 'walk', 'airplane']
print(animal_to_locomotion)
print(len(animal_to_locomotion))

animal_to_locomotion['kangaroo'].append('airplane')
print(animal_to_locomotion)
print(len(animal_to_locomotion))

animal_to_locomotion['frog'] = ['tapdance']
print(animal_to_locomotion)
print(len(animal_to_locomotion))

animal_to_locomotion['dolphin'] = animal_to_locomotion['fish']
print(animal_to_locomotion)
print(len(animal_to_locomotion))

# animal_to_locomotion['orangutan'].append('brachiate')
# print(animal_to_locomotion)
# print(len(animal_to_locomotion))

# Question 3:

from typing import List, Dict

def express_checkout(product_to_quantity: Dict[str, int]) -> bool:
    """Return True if and only if the grocery order in product_to_quantity
    qualifies for the express checkout. (Express checkout is for grocery
    order with 8 or fewer items). product_to_quantity maps products to the
    numbers of those items in the grocery order.

    >>> express_checkout({'banana': 3, 'soy milk': 1, 'peanut butter': 1})
    True
    >>> express_checkout({'banana': 3, 'soy milk': 1, 'twinkie': 5})
    False
    """
    count = 0

    for item in product_to_quantity:
        count += product_to_quantity[item]

    if count <= 8:
        return True

    return False

print(express_checkout({'banana': 3, 'soy milk': 1, 'peanut butter': 1}))
print(express_checkout({'banana': 3, 'soy milk': 1, 'twinkie': 5}))

# Question 4:

from typing import Dict, List

def build_placements(shoes: List[str]) -> Dict[str, List[int]]:
    """Return a dictionary where each key is a company and each value is a
    list of placements by people wearing shoes made by that company.

    >>> result = build_placements(['Saucony', 'Asics', 'Asics', 'NB', 'Saucony', \
    'Nike', 'Asics', 'Adidas', 'Saucony', 'Asics'])
    >>> result == {'Saucony': [1, 5, 9], 'Asics': [2, 3 ,7, 10], 'NB': [4], \
    'Nike': [6], 'Adidas': [8]}
    True
    """
    places = {}

    for i in range(len(shoes)):
        if shoes[i] in places:
            places[shoes[i]].append(i + 1)

        else:
            places[shoes[i]] = [i + 1]

    return places

result = build_placements(['Saucony', 'Asics', 'Asics', 'NB', 'Saucony', \
                           'Nike', 'Asics', 'Adidas', 'Saucony', 'Asics'])
print(result == {'Saucony': [1, 5, 9], 'Asics': [2, 3 ,7, 10], 'NB': [4], \
                 'Nike': [6], 'Adidas': [8]})
