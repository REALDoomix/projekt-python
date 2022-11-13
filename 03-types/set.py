'''
 Set je množina jedinečných hodnot
 Set je kolekce, která není zindexovaná ani seřazená.
 V pythonu sety jsou psány ve vlnitých závorkách.
'''
my_set = {2, 3, 9, 7}
print('Množina my_set: ', my_set)
print('Typ my_set: ', type(my_set))

# Vytvoření množiny ze seznamu hodnot (list)
numbers = [1, 4, 1, 5, 3, 3, 1, 2, 8, 2]
print(f'Proměnná numbers - seznam (list): {numbers}')
set_numbers = set(numbers)
print(f'Proměnná set_numbers - množina (set): {set_numbers}')

# Vytvoření množiny jedinečných znaků z řetězce
chars = sorted(list('Hello world'))
set_chars = set(chars)
print(f'Uspořádaná množina (set) jedinečných hodnot: {set_chars}')

# Jakmile je vytvořen set není možné položky měnit, ale můžete nějaké přidat.
# Abyste přidali jednu položku do setu použíjte add() metodu.
set_chars.add('V')

# Abyste přidali více než jednu položku do setu použíjte update() metodu.
set_chars.update('X', 'Y', 'Z')

# Abyste odstranili položku v setu, použíjte metodu remove(), nebo discard()
set_chars.remove('H')
print(f'Proměnná set_chars: {set_chars}')

# Použitím metody clear() se set vyprázdní.
set_chars.clear()

# Klíčové slovo del kompletně smaže celý set:
del set_chars

# Přístup k hodnotám množiny
# V setu se nedokážete dostat k předmětu pomocí indexu, jelikož set je neseřazený (tudíž nemá žádný index)
# my_set[1]


# Ale můžete loopovat skrz set pomocí for loopu, nebo si ověřit, zda se určitá hodnota vyskytuje v setu, pomocí použití klíčového slova "in".
for x in my_set:
  print(x)

'''
Množinové operace
'''
# Sjednocení množin
print(f'set_numbers | my_set: {set_numbers | my_set}')
print(f'set_numbers.union(my_set): {set_numbers.union(my_set)}')
# Průnik množin
print(f'set_numbers & my_set: {set_numbers & my_set}')
print(f'set_numbers.intersection(my_set): {set_numbers.intersection(my_set)}')
# Rozdíl množin
print(f'set_numbers - my_set: {set_numbers - my_set}')
print(f'set_numbers.difference(my_set): {set_numbers.difference(my_set)}')
# Doplněk množin
print(f'set_numbers ^ my_set: {set_numbers ^ my_set}')
print(f'set_numbers.symmetric_difference(my_set): {set_numbers.symmetric_difference(my_set)}')
# Zjištění zda množina obsahuje hodnotu
print(f'1 in set_numbers: {1 in set_numbers}')
