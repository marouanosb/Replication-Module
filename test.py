from replc import replicate
import pytest


def test_replicate():
    assert replicate(2, 4, lambda x: x, 7) == [[7,7,7,7],[7,7,7,7]]