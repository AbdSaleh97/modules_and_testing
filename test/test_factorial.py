import pytest
from factorial_module.factorial_module import *

def test_rec_fac_test1():
    actual = factorial_rcursioun(1)
    expected = 1
    assert actual == expected

def test_rec_fac_test2():
    actual = factorial_rcursioun(5)
    expected = 120
    assert actual == expected

def test_rec_fac_test3():
    actual = factorial_rcursioun(6)
    expected = 720
    assert actual == expected


def test_iter_fac_test1():
    actual = factorial_iterative(1)
    expected = 1
    assert actual == expected

def test_iter_fac_test2():
    actual = factorial_iterative(5)
    expected = 120
    assert actual == expected

def test_iter_fac_test3():
    actual = factorial_iterative(3)
    expected = 6
    assert actual == expected


def test_clumsy_with_n_equals_1():
    assert clumsy(1) == 1

def test_clumsy():
    assert clumsy(10) == 12

def test_clumsy_with_n_equals_0():
    assert clumsy(0) == 0 

def test_clumsy():
    assert clumsy(6) == 8

def test_clumsy_with_edge_case():
    assert clumsy(2) == 2