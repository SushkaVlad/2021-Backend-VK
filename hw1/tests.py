import unittest
from parameterized import parameterized
from tictac import TicTacGame


class TestGame(unittest.TestCase):
    """TestClass for TicTac game"""

    def setUp(self):
        """method to execute before each test"""
        self.game = TicTacGame()
        self.game.player1.update({'nick': 'test1', 'token': 'X'})
        self.game.player2.update({'nick': 'test2', 'token': 'Y'})

    @parameterized.expand([
        (1, 'X'), (2, 'X'), (3, 'X'), (4, 'X'), (5, 'X'), (6, 'X'), (7, 'X'), (8, 'X'), (9, 'X'),
        (1, 'O'), (2, 'O'), (3, 'O'), (4, 'O'), (5, 'O'), (6, 'O'), (7, 'O'), (8, 'O'), (9, 'O')
    ])
    def test_update_field(self, num, token):
        """tests the filling of the game cell"""
        self.game.update_field(num, token)
        self.assertEqual(self.game.fields[num - 1], token)

    @parameterized.expand([
        ([1, 2, 3],), ([4, 5, 6],), ([7, 8, 9],), ([1, 4, 7],),
        ([2, 5, 8],), ([3, 6, 9],), ([1, 5, 9],), ([3, 5, 7],)
    ])
    def test_win(self, comb):
        """tests check of the winner"""
        for i in comb:
            self.game.update_field(i, self.game.player2['token'])
        self.assertTrue(self.game.check_winner(self.game.player2))

    @parameterized.expand([
        ([1, 2, 4],), ([4, 7, 6],), ([2, 8, 9],), ([1, 3, 7],),
        ([1, 5, 8],), ([3, 4, 9],), ([1, 8, 9],), ([3, 5, 1],)
    ])
    def test_not_win(self, comb):
        """tests check of not winner"""
        for i in comb:
            self.game.update_field(i, self.game.player2['token'])
        self.assertFalse(self.game.check_winner(self.game.player2))

    def test_draw(self):
        """tests check of draw"""
        draw_token_seq = ('X', 'O', 'X', 'O', 'O', 'X', 'X', 'X', 'O')
        for ind, token in enumerate(draw_token_seq):
            self.game.update_field(ind+1, token)
        self.assertFalse(self.game.check_winner(self.game.player1))
        self.assertFalse(self.game.check_winner(self.game.player2))
        self.assertEqual(self.game.move_counter, 9)

    @parameterized.expand(['0', '11', '5a', 'abc', '-9'])
    def test_validate_incorrect_input(self, val):
        """tests incorrect input"""
        self.assertFalse(self.game.validate_input(val))

    @parameterized.expand([
        (1, 'X'), (2, 'X'), (3, 'X'), (4, 'X'), (5, 'X'), (6, 'X'), (7, 'X'), (8, 'X'), (9, 'X'),
        (1, 'O'), (2, 'O'), (3, 'O'), (4, 'O'), (5, 'O'), (6, 'O'), (7, 'O'), (8, 'O'), (9, 'O')
    ])
    def test_validate_not_empty_input(self, num, token):
        """tests input in not empty field"""
        self.game.update_field(num, token)
        self.assertFalse(self.game.validate_input(num))

    @parameterized.expand(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    def test_validate_correct_input(self, val):
        """tests correct input"""
        self.assertTrue(self.game.validate_input(val))

    def test_reset(self):
        """tests the reset before a new game"""
        self.game.update_field(4, self.game.player1['token'])
        self.game.update_field(7, self.game.player2['token'])
        self.game.reset()
        self.assertDictEqual(self.game.player1, dict())
        self.assertDictEqual(self.game.player2, dict())
        self.assertEqual(self.game.fields, [1, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == '__main__':
    unittest.main()
