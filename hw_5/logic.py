from decouple import config
import random
class Player:
    def __init__(self, name):
        self.__name = name
        self.__capital = int(config('START_CAPITAL'))
        self.__attempts = int(config('NUMBER_OF_ATTEMPTS'))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def capital(self):
        return self.__capital

    @capital.setter
    def capital(self, value):
        self.__capital = value

    @property
    def attempts(self):
        return self.__attempts

    @attempts.setter
    def attempts(self, value):
        self.__attempts = value

    def __str__(self):
        return f"{self.__name}------ Капитал: {self.__capital} Осталось попыток: {self.__attempts}"

def start_game():
    player = Player("Joker")
    show_stats(player)
    while not game_over(player):
        play_round(player)
        show_stats(player)


def play_round(player):
    try:
        random_num = random.randint(1, 10)
        player_bit = int(input(f"Введите свою ставку" ))
        if player_bit > player.capital:
            print("Вы не можете поставить больше чем у вас есть ")
            return play_round(player)
        if player_bit < 0:
            print("Вы не можете ввести отрицательные числа ")
            return play_round(player)
        player_num = int(input(f"Введите число на которое хотите поставить "))
        if player_num < int(config("MIN_NUM")) or player_num > int(config("MAX_NUM")):
            print(f"Не выходите с задного диопазона ")
            return play_round(player)
        if random_num == player_num:
            print(f"Вы угадали! Ваш общий банк вырос на {player_bit}")
            player.capital += player_bit
            player.attempts = int(config("NUMBER_OF_ATTEMPTS"))
        else:
            print(f"Вы ошиблись ваш банк уменьшился на {player_bit} загаданное число было {random_num}")
            player.capital -= player_bit
            player.attempts -= 1
    except ValueError:
        print("Ошибка введите корректное число ")
def game_over(player):
    if player.capital <= 0 or player.attempts == 0:
        print("Вы проиграли(")
        return True

def show_stats(player):
    print(f"{player.name}! Ваш банк состовляет : {player.capital} Попыток осталось : {player.attempts}")











        

        