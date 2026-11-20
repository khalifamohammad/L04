import os
import sqlite3
import subprocess

import pytest

import exercise2
from exercise2 import *


# bug report 1
def test_r1_is_passing():
    assert is_passing(5) is True


# bug report 2
def test_r2_is_valid_password():
    assert is_valid_password("12345678") is True


# bug report 3
def test_r3_clamp_bug():
    assert clamp(15, 1, 10) == 10
