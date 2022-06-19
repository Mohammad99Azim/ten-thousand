import pytest
from tests.flo import diff
from ten_thousand.ten_thousands import Game


def test_hot_dice():
    game = Game()
    diffs = diff(game.play, "tests/version_3/hot_dice.sim.txt")
    assert not diffs, diffs


def test_cheat_and_fix():
    game = Game()
    diffs = diff(game.play, "tests/version_3/cheat_and_fix.sim.txt")
    assert not diffs, diffs


def test_repeat_roller():
    game = Game()
    diffs = diff(game.play, "tests/version_3/repeat_roller.sim.txt")
    assert not diffs, diffs


def test_zilcher():
    game = Game()
    diffs = diff(game.play, "tests/version_3/zilcher.sim.txt")
    assert not diffs, diffs
