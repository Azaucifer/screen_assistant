import sqlite3


def init_db():
    db = sqlite3.connect("assistant.db")

    db.execute(
        """
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            content TEXT NOT NULL
        )
        """
    )

    db.commit()
    db.close()


def save_message(role, content):
    db = sqlite3.connect("assistant.db")

    db.execute(
        "INSERT INTO messages (role, content) VALUES (?, ?)",
        (role, content),
    )

    db.commit()
    db.close()


def get_messages():
    db = sqlite3.connect("assistant.db")

    messages = db.execute(
        "SELECT id, role, content FROM messages"
    ).fetchall()

    db.close()

    return messages


if __name__ == "__main__":
    init_db()
