from ten_thousand.ten_thousands import Game
from tests.flo import diff


def test_quitter_sim():
    game = Game()

    diffs = diff(game.play, 'version_2/quitter.sim.txt')
    assert not diffs, diffs


def test_one_and_done_sim():
    game = Game()

    diffs = diff(game.play, 'version_2/one_and_done.sim.txt')
    assert not diffs, diffs

def test_bank_one_roll_then_quit_sim():
    game = Game()

    diffs = diff(game.play, 'version_2/bank_one_roll_then_quit.sim.txt')
    assert not diffs, diffs


def test_bank_first_for_two_reounds():
    game = Game()

    diffs = diff(game.play, 'version_2/bank_first_for_two_rounds.sim.txt')
    assert not diffs, diffs