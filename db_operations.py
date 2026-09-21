import psycopg2

DATABASE_NAME = "library_db"

'''
3 Operations:
  Create the books table
  Insert sample books
  Display older books
'''


def database_operations():
    connection = None
    cursor = None

    # Connect to the local database
    try:
        connection = psycopg2.connect(dbname=DATABASE_NAME)

        # Cursor allows Python to send SQL commands to PostgreSQL
        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                author VARCHAR(255) NOT NULL,
                publication_year INT
            );
            """
        )

        # Count existing rows in the books table to prevent duplicates
        cursor.execute("SELECT COUNT(*) FROM books;")

        # Returns one database row as a tuple, index 0 fetches the number of books
        book_count = cursor.fetchone()[0]

        # Insert only when the table is empty
        if book_count == 0:
            sample_books = [
                ("The Great Gatsby", "F. Scott Fitzgerald", 1925),
                ("Project Hail Mary", "Andy Weir", 2021)
            ]

            # Run the INSERT statement once for each tuple
            cursor.executemany(
                """
                INSERT INTO books (title, author, publication_year)
                VALUES (%s, %s, %s);
                """,
                sample_books,
            )
        # Commit to save the changes
        connection.commit()

        # Fetches only books published before the year 2000
        cursor.execute(
            """
            SELECT id, title, author, publication_year
            FROM books
            WHERE publication_year < 2000
            ORDER BY publication_year;
            """
        )

        # Return and print the results
        books = cursor.fetchall()
        print("Books published before 2000:")

        for book in books:
            print(
                f"ID: {book[0]}, "
                f"Title: {book[1]}, "
                f"Author: {book[2]}, "
                f"Year: {book[3]}"
            )

    # Error Handling
    except psycopg2.Error as error:
        if connection is not None:
            connection.rollback()
        print(f"Database operation failed: {error}")

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()


if __name__ == "__main__":
    database_operations()
