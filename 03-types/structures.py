def char_frequency(txt):
    return sorted([(char, txt.count(char)) for char in set (txt)],
                  reverse=True, key=lambda i: i[1])

def read_txtfile(filename):
    f = open(filename, "r", encoding = 'utf8')
    return f.read()

def write_txtfile(filename, text):
    f = open(filename, "w", encoding='utf8')
    f.write(text)
    f.close()
    return True

pokus = 'Tři sta třicet tři stříbrných stříkaček přestříkalo přes tři sta třicet tři stříbrných střech.'
print(pokus)
print(char_frequency(pokus))
write_txtfile('frekvence.txt',str(char_frequency(pokus)))


