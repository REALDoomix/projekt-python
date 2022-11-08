"""
Zadání:
S využitím principů OOP vytvořte simulaci jednoduché hry, v níž se v zápase (Match) virtuálně utkají vždy dva hráči (Player).
Zápas tvoří symbolické souboje (výměny) na 10 vítězných bodů.
Hráč získává bod, když hodí vyšší hodnotu symbolickou kostkou než jeho protihráč.
Objekty hráčů mohou být načteny z datového souboru - players.json.
"""

"""
Importované moduly
"""
# Modul datetime používáme pro práci s datem a časem
import datetime
# Modul enum používáme k vytvoření výčtových typů
from enum import Enum
# Modul random obsahuje různé metody pro generování náhodných čísel
from random import randrange
# Modul files obsahuje předprogramované metody pro načítání různých typů souborů (JSON, CSV, TXT)
from files import jsonfile_read

"""
Třídy
"""
class Sex(Enum):
    """
    Třída typu Enum používaná pro výčet přípustných hodnot.
    V tomto případě pro identifikaci pohlaví.
    """
    male = 'man'
    female = 'woman'


class Person:
    """
    Třída Person (odvozena z bázové třídy object)
    """
    def __init__(self, nickname: str, sex: Sex):
        """
        Inicializační metoda konstruktoru
        * nickname - přezdívka osoby
        * sex - pohlaví osoby (podle výčtového typu Sex)
        """
        self.nickname = nickname
        self.sex = sex
        # Datum a čas vzniku objektu
        self.__birth = datetime.datetime.now()

    def __str__(self):
        """
        Magická metoda pro vyjádření objektu v textové podobě - str(objekt)
        """
        return f'Přezdívka: {self.nickname}, pohlaví: {self.sex.value} ' \
               f'zrození: {self.__birth}'

    def get_birth(self):
        return self.__birth

    # Dekorátor vytvářející property (vlastnost) sex
    @property
    def sex(self):
        # Vrací hodnotui zapouzdřeného (privátního) atributu self.__sex
        return self.__sex

    # Dekorátor určený pro bezpečné nastavení hodnoty pro property sex
    @sex.setter
    def sex(self, sex):
        # Kontrola, zdali se zadaná hodnota vyskytuje ve výčtopvém typu Sex
        if sex in Sex:
            self.__sex = sex
        else:
            # Jestliže zadaná hodnota tomuto typu neodpovídá, vyvolá se výjimka (raise)
            raise ValueError("Sex value not valid")

    # Metoda vrací počet sekund od vzniku objektu
    def get_seconds_from_birth(self):
        actual_time = datetime.datetime.now()
        return int((actual_time - self.__birth).total_seconds())


"""
Třída Player je odvozena (princip dědičnosti) od předka Person
"""
class Player(Person):
    def __init__(self, nickname: str, sex: Sex, state: str):
        """
        Inicializační metoda konstruktoru obsahuje navíc parametr state (zkratka státu)
        """
        # Vyvolá inicializační metodu konstruktoru předka (super())
        super().__init__(nickname, sex)
        # Inicializace atributů objektu
        self.state = state
        self.count_of_games = 0
        self.wins = 0
        self.score = {'plus': 0, 'minus': 0}

    def __str__(self):
        return f'{super().__str__()}, state: {self.state}'

    @property
    def wins(self):
        return self.__wins

    @wins.setter
    def wins(self, value):
        if value < 0:
            raise ValueError("Property wins must not be a negative value")
        else:
            self.__wins = value

    # Metoda vyhodnotí procentuální úspěšnost hráče
    def win_rate(self):
        try:
            rate = self.wins / self.count_of_games * 100
        except ZeroDivisionError as error:
            print(f'Error: {error}')
            return False
        else:
            # Vrací reálné číslo formátované na 2 desetinná místa
            return float("{:.2f}".format(rate))


"""
Třída Match řeší virtuální zápas mezi dvěma hráči
"""
class Match:
    def __init__(self, house_player: Player, guest_player: Player):
        """
        Inicializační metoda konstruktoru
        * house_player - domácí hráč
        * guest_player - hostující hráč
        """
        self.h_player = house_player
        self.g_player = guest_player
        # Uložení data a času začátku zápasu (privátní atribut)
        self.__datetime = datetime.datetime.now()
        # Body domácího hráče
        self.hp_points = 0
        # Body hostujícího hráče
        self.gp_points = 0
        # Seznam (list) obsahující vývoj skóre (privátní atribut)
        self.__history = []

    def __str__(self):
        return f'{self.h_player.nickname} vs. {self.g_player.nickname} {self.score()}'

    # Vytvoření properties pro bezpečné uložení objektů obou hráčů
    @property
    def h_player(self):
        return self.__hplayer

    @h_player.setter
    def h_player(self, player):
        # Kontrola, zda zadaný objekt je opravdu instancí třídy Player
        if isinstance(player, Player):
            self.__hplayer = player
        else:
            # V případě nesprávného typu (třídy) je vyvolána výjimka
            raise TypeError("h_player must be instance Player")

    @property
    def g_player(self):
        return self.__gplayer

    @g_player.setter
    def g_player(self, player):
        if isinstance(player, Player):
            self.__gplayer = player
        else:
            raise TypeError("g_player must be instance Player")

    # Privátní metoda simuluje hody kostkou pro oba hráče
    def __roll(self):
        while True:
            # Jsou generována náhodná čísla v rozmezí 1 až 6
            hp = randrange(1, 7)
            gp = randrange(1, 7)
            # Když jsou hody rozdílné, je přerušen cyklus while
            if hp != gp:
                break
        # Ternární operátor zajistí návratovou hodnotu 0 (když hodil více domácí), nebo 1 (větší hod měl host)
        return 0 if hp > gp else 1

    # Metoda simuluje odehrání celého zápasu až do vítězných 10 bodů získaných jedním z hráčů
    def play(self):
        while self.hp_points < 10 and self.gp_points < 10:
            # Jestliže symbolickou výměnu vyhrál domácí hráč (metoda __roll vrátila 0)
            if self.__roll() == 0:
                # Přičtení bodů domácímu hráči
                self.hp_points += 1
            else:
                # Přičtení bodů hostujícímu hráči
                self.gp_points += 1
            # Přidá změnu skóre do historie zápasu
            self.__history.append(self.score())
        # Provedou se změny celkového skóre v objektech obou hráčů
        self.h_player.score['plus'] += self.hp_points
        self.h_player.score['minus'] += self.gp_points
        self.g_player.score['plus'] += self.gp_points
        self.g_player.score['minus'] += self.hp_points
        # Vítěznému hráči se zvýší hodnota uložená v atributu wins
        if self.hp_points > self.gp_points:
            self.h_player.wins += 1
        else:
            self.g_player.wins += 1

    # Metoda vrací skóre zápasu v podobě tuple (např. (10, 8))
    def score(self):
        return self.hp_points, self.gp_points

    # Metoda vrací obsah privátního atributu self.__history
    def get_history(self):
        return self.__history

"""
Metoda umožňující hromadné načtení hráčů ze souboru JSON
"""
def load_players(json_file: str):
    players = []
    try:
        data = jsonfile_read(json_file)
    except Exception as error:
        print(f'Error: {error}')
        return False
    else:
        for row in data:
            players.append(Player(row['nickname'], Sex(row['sex']), row['state']))
    return players


"""
Testování funkčnosti jednotlivých částí modulu
"""
person = []

person.append(Person('Alois', Sex.male))
person.append(Person('Anna', Sex.female))

print(person[0].get_birth(), person[1].get_seconds_from_birth())