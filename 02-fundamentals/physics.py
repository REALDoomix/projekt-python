'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.80665 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.6236 #? měsíční gravitace
SPEED_OF_LIGHT = 300000 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''

def casRychlostiSvetla(delka):
    '''

    Tato funkce bere délku v kilometrech a
    returnuje výsledek délky / rychlost světla
    tímto vypíše jak dlouho by trvalo tuto vzdálenost urazit rychlostí světla

    '''
    return delka / SPEED_OF_LIGHT

def casRychlostiZvuku(delka):
    '''

    Tato funkce bere délku v kilometrech a
    returnuje výsledek délky / rychlost zvuku
    tímto vypíše jak dlouho by trvalo tuto vzdálenost urazit rychlostí zvuku

    '''
    return (delka / SPEED_OF_SOUND) / 60

def potencialniEnergie(vaha, vyskaZdvihu):
    '''

    Tato funkce bere váhu v kilogramech a dále výšku zdvihu
    returnuje výsledek vzorce Ep = m * g * h , kde
    m = váha objektu, g = gravitační konstanta, h = výška zdvihu
    Tímto vypíše potenciální energii objektu o váze m ve výšce h

    '''

    return vaha * EARTH_GRAVITY * vyskaZdvihu

def vahaNaMesici(vaha):
    '''

    Tato funkce bere váhu na zemi v kilogramech a
    returnuje kolik by osoba, či objekt vážila na měsíci

    '''

    return vaha / (EARTH_GRAVITY / MOON_GRAVITY)