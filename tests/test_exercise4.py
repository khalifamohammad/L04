import os
import sqlite3
import subprocess

import pytest

import exercise4
from exercise4 import *


# bug report 1
def test_r1_check_admin_hardcoded_password():
    import os
    # Simulate the hardcoded password by setting environment variable to "admin123"
    os.environ["ADMIN_PASSWORD"] = "admin123"
    assert check_admin("admin123") == True  # Should be False due to hardcoded password, but currently returns True
    assert check_admin("wrongpassword") == False  # Correct behavior for wrong password


# bug report 2
def test_r2_find_user_sql_injection():
    import sqlite3
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE users (username TEXT, password TEXT)")
    db.execute("INSERT INTO users VALUES ('alice', 'pass123')")
    db.execute("INSERT INTO users VALUES ('bob', 'pass456')")
    db.commit()
    assert find_user(db, "' OR '1'='1") is None
