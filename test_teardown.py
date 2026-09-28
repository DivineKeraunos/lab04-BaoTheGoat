import sqlite3
import pytest


@pytest.fixture
def db(tmp_path):
    print("\n[setup] creating database with schema and seed data")
    conn = sqlite3.connect(tmp_path / "app.db")
    conn.execute(
        """
        CREATE TABLE users (
            id     INTEGER PRIMARY KEY,
            email  TEXT UNIQUE NOT NULL,
            active INTEGER DEFAULT 1
        )
        """
    )
    conn.execute("INSERT INTO users (email) VALUES ('seed@example.com')")
    conn.commit()

    yield conn  # the test runs here

    print("\n[teardown] closing connection (tmp_path is deleted by pytest)")
    conn.close()


def count_users(conn):
    return conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]


def test_add_user(db):
    db.execute("INSERT INTO users (email) VALUES ('new@example.com')")
    db.commit()

    assert count_users(db) == 2  # seed + new


def test_duplicate_email_is_rejected(db):
    with pytest.raises(sqlite3.IntegrityError):
        db.execute("INSERT INTO users (email) VALUES ('seed@example.com')")
        
    assert count_users(db) == 1
