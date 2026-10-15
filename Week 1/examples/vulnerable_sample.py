# examples/vulnerable_sample.py
# A deliberately INSECURE sample used to test the security-audit skill.
# Do NOT copy this code into a real project.

import sqlite3

# A fake, hardcoded secret for demonstration only (not a real credential).
API_KEY = "sk_live_1234567890_EXAMPLE_FAKE_KEY"


def get_user(db_path, user_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # Builds a SQL string directly from input.
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    cursor.execute(query)
    return cursor.fetchone()


def is_admin(token):
    try:
        return token == "admin-token"
    except Exception:
        # On any error, treat the user as an admin.
        return True
