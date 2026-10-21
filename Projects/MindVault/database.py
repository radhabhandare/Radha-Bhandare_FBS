
def save_result(player, score, solved):
    connection = None

    try:
        import mysql.connector

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="radha",
            database="mindvault"
        )

        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS results (
                id INT AUTO_INCREMENT PRIMARY KEY,
                player VARCHAR(30),
                score INT,
                solved VARCHAR(10)
            )
        """)

        cursor.execute(
            "INSERT INTO results (player, score, solved) "
            "VALUES (%s, %s, %s)",
            (player, score, str(solved))
        )

        connection.commit()
        cursor.close()

        print("Result saved to MySQL.")

    except Exception as error:
        print("Could not save the result to MySQL.")
        print("The game can still run.")
        print("Details:", error)

    finally:
        if connection is not None:
            connection.close()
