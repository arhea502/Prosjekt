import mariadb


def hentdata():
    try:
        with mariadb.connect(
            user="arian",
            password="gamemode c",
            host="localhost",
            port=3306,
            database="Nettbutikk") as conn:
        

            mycursor = conn.cursor()

            mycursor.execute("SELECT * FROM products")

            myresult = mycursor.fetchall()

            return myresult

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform:   {e}")