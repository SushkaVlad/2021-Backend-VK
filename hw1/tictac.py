class TicTacGame:
    """class with main methods for TicTac game"""
    def __init__(self):
        """constructor of the class"""
        self.player1 = {}
        self.player2 = {}
        self.fields = list(range(1, 10))
        self.move_counter = 0
        self.win_comb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7),
                         (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def show_board(self):
        """prints game field"""
        print("""
        -------------
        | {0} | {1} | {2} |
        -------------
        | {3} | {4} | {5} |
        -------------
        | {6} | {7} | {8} |
        -------------
        """.format(*self.fields))

    def start_game(self):
        """starts game (input of players' names)"""
        print("Добро пожаловать в игру 'Крестики-нолики' для двоих!")
        nick1 = input("Введите имя первого игрока (X): ")
        self.player1.update({'nick': nick1, 'token': 'X'})
        nick2 = input("Введите имя второго игрока (O): ")
        self.player2.update({'nick': nick2, 'token': 'O'})
        print("По древним правилам данной игры ответственность за первый ход возлагается на X!")

    def validate_input(self, move):
        """checks validity of moves"""
        try:
            move = int(move)
        except ValueError:
            print("Некорректный ввод. Вы ввели не число")
            return False
        if move < 1 or move > 9:
            print("Некорректный ввод. Введите число от 1 до 9.")
            return False
        if self.fields[move - 1] != move:
            print("Данная клетка уже занята")
            return False
        return True

    def update_field(self, move, token):
        """puts Tic or Tac on the game field"""
        self.fields[move - 1] = token

    def check_winner(self, player):
        """checks if someone has already won"""
        for comb in self.win_comb:
            if self.fields[comb[0]] == self.fields[comb[1]] == \
                    self.fields[comb[2]] == player['token']:
                return True
        return False

    def reset(self):
        """resets variables for new game"""
        self.player1.clear()
        self.player2.clear()
        self.fields = list(range(1, 10))
        self.move_counter = 0


def game_logic():
    """determines logic (algorithm) of the game"""
    win = False
    cur_move = 0
    game.start_game()
    while not win:
        game.show_board()
        if game.move_counter % 2 == 0:
            cur_player = game.player1
        else:
            cur_player = game.player2
        valid = False
        while not valid:
            cur_move = input(f" {cur_player['nick']}, куда поставим {cur_player['token']} ?")
            valid = game.validate_input(cur_move)
        game.update_field(int(cur_move), cur_player['token'])
        game.move_counter += 1
        if game.move_counter > 4:
            tmp = game.check_winner(cur_player)
            if tmp:
                print(f"{cur_player['nick']}, игравший за {cur_player['token']} победил!!!")
                break
        if game.move_counter == 9:
            print("Ничья!")
            break
    game.show_board()


if __name__ == '__main__':
    game = TicTacGame()
    while True:
        game_logic()
        play_again = input("Хотите ли сыграть еще раз? (да/нет)")
        while play_again not in ("да", "нет"):
            play_again = input("Неверный ввод. Хотите ли сыграть еще раз? (да/нет)")
        if play_again == "нет":
            break
        game.reset()
    print("До свидания!")
