from logic import start_game,show_stats,play_round,game_over,Player
def start_game():
    player = Player("Joker")
    show_stats(player)
    while not game_over(player):
        play_round(player)
        show_stats(player)
start_game()