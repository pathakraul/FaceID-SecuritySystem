# -*- coding: utf-8 -*-

import pytest
from faceid_securitysystem.skeleton import fib

__author__ = "Rahul Pathak"
__copyright__ = "Rahul Pathak"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
