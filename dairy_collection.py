
"""Dairy milk collection ledger."""

import hashlib
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    """
    CREATE TABLE milk (
        id INTEGER PRIMARY KEY,
        farmer TEXT,
        litres REAL,
        fat REAL,
        day TEXT
    )
    """
)


def recordMilk(conn, farmer, litres, fat, day):
    """Record a farmer's milk delivery."""
    conn.execute(
        """
        INSERT INTO milk (farmer, litres, fat, day)
        VALUES (?, ?, ?, ?)
        """,
        (farmer, litres, fat, day),
    )
    conn.commit()


def farmerToken(farmer):
    """Generate a SHA-256 digest for a farmer's name."""
    return hashlib.sha256(farmer.encode("utf-8")).hexdigest()


def dailyTotal(conn, day):
    """Calculate the total milk collected on a given day."""
    rows = conn.execute(
        "SELECT litres FROM milk WHERE day = ?",
        (day,),
    ).fetchall()
    return "Total: %.1f litres" % sum(row[0] for row in rows)


def topFarmer(conn):
    """Return the farmer with the highest total delivery."""
    rows = conn.execute(
        """
        SELECT farmer, SUM(litres)
        FROM milk
        GROUP BY farmer
        ORDER BY SUM(litres) DESC
        LIMIT 1
        """
    ).fetchone()
    return rows[0] if rows is not None else "No collections recorded"


def printSlip(farmer):
    """Print a collection-slip message without invoking a shell."""
    print("Printing slip for {}".format(farmer))


def lowFat(conn):
    """Find farmers whose milk fat is missing or below 3.5."""
    rows = conn.execute("SELECT farmer, fat FROM milk").fetchall()
    return [
        farmer for farmer, fat in rows
        if fat is None or fat < 3.5
    ]


def main():
    """Run a short dairy collection demonstration."""
    recordMilk(conn, "Gopal", 12.5, 4.1, "Mon")
    recordMilk(conn, "Lata", 20.0, 3.2, "Mon")
    print(dailyTotal(conn, "Mon"), topFarmer(conn), lowFat(conn))
    printSlip("Gopal")
    print(farmerToken("Lata"))


main()
