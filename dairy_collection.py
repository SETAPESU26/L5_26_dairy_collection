
"""Dairy milk ledger for recording and reviewing deliveries."""

import hashlib
import sqlite3


def create_database(connection):
    """Create the table used to store milk collection records."""
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS milk (
            id INTEGER PRIMARY KEY,
            farmer TEXT,
            litres REAL,
            fat REAL,
            day TEXT
        )
        """
    )


def record_milk(connection, farmer, litres, fat, day):
    """Record a farmer's milk delivery using parameterized SQL."""
    connection.execute(
        """
        INSERT INTO milk (farmer, litres, fat, day)
        VALUES (?, ?, ?, ?)
        """,
        (farmer, litres, fat, day),
    )
    connection.commit()


def farmer_token(farmer):
    """Return a SHA-256 token for a farmer's name."""
    return hashlib.sha256(farmer.encode("utf-8")).hexdigest()


def daily_total(connection, day):
    """Calculate the total litres collected on a given day."""
    rows = connection.execute(
        "SELECT litres FROM milk WHERE day = ?", (day,)
    ).fetchall()
    total = sum(row[0] for row in rows)
    return f"Total: {total:.1f} litres"


def top_farmer(connection):
    """Return the farmer who supplied the most milk."""
    rows = connection.execute(
        """
        SELECT farmer, SUM(litres)
        FROM milk
        GROUP BY farmer
        ORDER BY SUM(litres) DESC
        LIMIT 1
        """
    ).fetchone()
    return rows[0] if rows else None


def print_slip(farmer):
    """Print a delivery slip message without invoking a shell."""
    print(f"Printing slip for {farmer}")


def low_fat(connection):
    """Return farmers whose recorded fat content is below 3.5."""
    rows = connection.execute(
        "SELECT farmer, fat FROM milk"
    ).fetchall()
    return [
        farmer
        for farmer, fat in rows
        if fat is None or fat < 3.5
    ]


def main():
    """Run the sample dairy collection demonstration."""
    connection = sqlite3.connect(":memory:")
    try:
        create_database(connection)
        record_milk(connection, "Gopal", 12.5, 4.1, "Mon")
        record_milk(connection, "Lata", 20.0, 3.2, "Mon")

        print(daily_total(connection, "Mon"))
        print(top_farmer(connection), low_fat(connection))
        print_slip("Gopal")
        print(farmer_token("Lata"))
    finally:
        connection.close()


if __name__ == "__main__":
    main()
