import unittest
from tictac import TicTacGame


class TestGame(unittest.TestCase):
    """TestClass for TicTac game"""
    def setUp(self):
        """method to execute before each test"""
        self.game = TicTacGame()
        self.game.player1.update({'nick': 'test1', 'token': 'X'})

    def test_update_field(self):
        """tests the filling of the game cell"""
        self.game.update_field(4, self.game.player1['token'])
        self.assertEqual(self.game.fields[3], 'X')

    def test_reset(self):
        """tests the reset before a new game"""
        self.game.reset()
        self.assertDictEqual(self.game.player1, dict())

    def test_win(self):
        """tests check of the winner"""
        for i in range(3, 8, 2):
            self.game.update_field(i, self.game.player1['token'])
        self.assertTrue(self.game.check_winner(self.game.player1))

    def test_validate_input(self):
        """tests check of moves' validity"""
        self.assertFalse(self.game.validate_input(10))


if __name__ == '__main__':
    unittest.main()
