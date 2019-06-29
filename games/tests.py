from django.test import TestCase
from .models import GameSession


# Create your tests here.
class GameSessionTestCase(TestCase):
    def setUp(self):
        GameSession.create(game='tic_tac_toe')
        GameSession.create(game='rock_paper_scissors')

    def test_objects_have_different_ids(self):
        tic_tac_toe = GameSession.get(game='tic_tac_toe')
        rock_paper_scissors = GameSession.get(game='rock_paper_scissors')
        self.assertGreater(rock_paper_scissors.id, tic_tac_toe.id)

    def test_save_and_load_game_state(self):
        tic_tac_toe = GameSession.get(game='tic_tac_toe')

        state = {'x': 1,
                 'y': 2}

        tic_tac_toe.state = state
        tic_tac_toe.save()

        del tic_tac_toe
        tic_tac_toe = GameSession.get(game='tic_tac_toe')
        self.assertEqual(tic_tac_toe.state, state)

        state = {'x': 3,
                 'y': 4}
        tic_tac_toe.state = state
        tic_tac_toe.save()

        del tic_tac_toe
        tic_tac_toe = GameSession.get(game='tic_tac_toe')
        self.assertEqual(tic_tac_toe.state, state)
