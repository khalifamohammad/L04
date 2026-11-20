You get one bug report and the Python file.
Write exactly ONE pytest test that proves the bug.
Rules:
- Answer with Python code only. No markdown, no ``` fences, no comments, no explanation.
- One function whose name starts with test_.
- Do not import the exercise functions: they are already imported. You may import standard modules (sqlite3, os) inside the test.
- Use the input from the Example line and assert the EXPECTED value, not the current output.
- The test must FAIL on the buggy code and PASS after the Fix.
- If the docstring says what to return for an empty or zero input, assert that return value. Never use pytest.raises in that case.
- Never use fake or mock objects. For a database, use a real in-memory sqlite3 database.
- For security bugs, assert that the attack FAILS.

Example for a hardcoded password:
def test_no_hardcoded_key():
    assert check_key("secret42") == False

Example for SQL injection:
def test_get_item_sql_injection():
    import sqlite3
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE items (name TEXT)")
    db.execute("INSERT INTO items VALUES ('apple')")
    assert get_item(db, "' OR '1'='1") is None
