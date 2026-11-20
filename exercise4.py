
import os


def check_admin(password):
    """True if the password is the admin password."""
    admin_password = os.getenv("ADMIN_PASSWORD", "")
    return admin_password != "" and password == admin_password


def find_user(db, username):
    """The user's row, or None if the username does not exist."""
    return db.execute(
        "SELECT * FROM users WHERE username = ?",
        (username,)
    ).fetchone()
