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
│ └── index2.html
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
