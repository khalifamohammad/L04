# Bug reports for exercise4.py

Line: 9
Problem: the secret key is hardcoded in the code, so anyone who reads the code can use it.
Example: check_admin("admin123") returns True, expected False.
Fix: ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "admin123")

Line: 14
Problem: the query is built with an f-string, so the input can change the SQL (SQL injection).
Example: find_user(db, "' OR '1'='1") returns a row, expected None.
Fix: return db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
