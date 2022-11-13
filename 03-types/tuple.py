'''
Tuples - neměnitelné n-tice hodnot (seřazený seznam prvků)
In Python tuples are written with round brackets.
'''

# Vytvoření tuples
numbers = (1, 2, 3)
print('numbers: ', numbers)
print('Type(numbers): ',type(numbers))

chars = tuple('Hello world')
print('chars: ', chars)
print('Type(chars): ',type(chars))

# To create a tuple with only one item, you have add a comma after the item, unless Python will not recognize the variable as a tuple.
colors = ('red',)
print('colors: ', colors)

# Součet tuples
print(f'chars + numbers: {chars + numbers}')

# Výpis hodnot
# Můžete specifikofvat range indexů, když specifikujete kde má začít a skončit range.
# Při specifikování range, returnová hodnota budde nový tuple se specifikovanými itemy.
print(f'chars[2:5]: {chars[2:5]}')

# Negativní indexy (t.j. např. -1) znamená, že se bude začínat od konce (-1 ukazuje na poslední položku, -2 ukazuje na předposlední položku atd.)
# Použíjte negativní indexy, pokud chcete začit vyhledávat od konce tuplu:
# Tento příklad returnuje předměty od indexu -4 (včetně) až po index -1 (kromě -1)
print(f'chars[-4:-1]: {chars[-4:-1]}')

# Abyste zjistili kolik předmětů má tuple, použíjte len() metodu:
print(f'len(chars): {len(chars)}')

# Zjištění prvního výskytu a počtu výskytu prvku
if 'l' in chars:
    print(f'chars.index("l"): {chars.index("l")}')
    print(f'chars.count("l"): {chars.count("l")}')

# Záměna hodnot proměnných
x = 10
y = 2
x, y = y, x
print(f'x: {x}, y: {y}')
