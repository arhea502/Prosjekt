# Terminoppgave: Nettbutikk

## Beskrivelse
Dette prosjektet er en enkel nettbutikk laget med **Flask** og **MariaDB** på en Raspberry Pi.  
Formålet er å hente data fra en database og vise det i en HTML-tabell ved hjelp av Flask og Jinja2.

---

## Teknologier brukt
- Python 3.13  
- Flask  
- MariaDB  
- Jinja2  
- Git / GitHub

---

## Filstruktur
Terminoppgave/
│
├── app.py
├── db.py
├── templates/
│   └── index2.html
├── .venv/
└── README.md


---

## Databaseoppsett
MariaDB må være installert og kjøre på localhost.  
Eksempel på databasefunksjon i `db.py`:

```python
import mariadb

def hentdata():
    try:
        with mariadb.connect(
            user="arian",
            password="####",
            host="localhost",
            port=3306,
            database="Nettbutikk"
        ) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products")
            return cursor.fetchall()
    except mariadb.Error as e:
        print(f"Database error: {e}")
        return []
```

# Flaske-applikasjon
``` python
from flask import Flask, render_template
from db import hentdata

app = Flask(__name__)

@app.route("/")
def home():
    data = hentdata()
    return render_template('index2.html', products=data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
```

HTML-template
<!DOCTYPE html>
<html lang="no">
<head>
    <meta charset="UTF-8">
    <title>Nettbutikk</title>
</head>
<body>

<h1>Produkter</h1>

<table border="1">
    <tr>
        <th>ID</th>
        <th>Navn</th>
        <th>Pris</th>
    </tr>

    {% for product in products %}
    <tr>
        <td>{{ product[0] }}</td>
        <td>{{ product[1] }}</td>
        <td>{{ product[2] }}</td>
    </tr>
    {% endfor %}

</table>

</body>
</html>

## Git / GitHub-håndtering

# Konfigurer bruker
git config --global user.name "Arian H"
git config --global user.email "arian@example.com"

# Sjekk status og remote
git status
git remote -v
Sørg for at det ikke finnes .git mapper i undermapper.

# Oppdater remote og push
git remote set-url origin https://github.com/arhea502/Prosjekt.git
git push -u origin main

# Sjekkliste før innlevering
git branch           # Sjekk at du er på main/master
git log --oneline    # Sjekk commits
find . -type d -name ".git"  # Kun ./.git skal vises


## Tips
source .venv/bin/activate

source .venv/bin/activate

# Oppdater .gitignore for å ignorere:

.venv/
__pycache__/
*.pyc
.DS_Store

    For mer lesbar Jinja2, kan du bruke dictionary-cursor:

cursor = conn.cursor(dictionary=True)





Slett alt untatt db.py og app.py
js fil slett.
alle httml untatt index. slett
controll z på db og app.py


def get_db_connection():
    return mariadb.connect(
        user="arian",
        password="gamemode c",
        host="localhost",
        port=3306,
        database="Nettbutikk"
    )


 Fancy T-Shirt
Fancy T-Shirt

Very cool shirt
299.00 NOK
Fancy T-Shirt
Fancy T-Shirt

Very cool shirt
299.00 NOK
Cool Hoodie
Cool Hoodie

Warm and stylish hoodie
599.00 NOK
Classic Jeans
Classic Jeans

Comfortable blue jeans
799.00 NOK
Sneakers
Sneakers

Lightweight everyday sneakers
999.00 NOK
Baseball Cap
Baseball Cap

Adjustable cotton cap
199.00 NOK
Leather Belt
Leather Belt

Genuine leather belt
349.00 NOK
Summer Shorts
Summer Shorts

Breathable summer shorts
399.00 NOK
Winter Jacket
Winter Jacket

Insulated jacket for cold weather
1499.00 NOK
Socks (3-pack)
Socks (3-pack)

Soft cotton socks
149.00 NOK
Beanie Hat
Beanie Hat

Warm knitted beanie
179.00 NOK
Running Shoes
Running Shoes

Comfortable shoes for running
1199.00 NOK
Denim Jacket
Denim Jacket

Classic denim jacket
1299.00 NOK
Graphic Tee
Graphic Tee

T-shirt with printed design
329.00 NOK
Zip Hoodie
Zip Hoodie

Hoodie with front zipper
649.00 NOK
Cargo Pants
Cargo Pants

Pants with multiple pockets
899.00 NOK