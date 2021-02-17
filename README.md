# Vilo Sky Paths

## Description

Vilo Sky Paths is intended to be a free, accessible website application that assists users in building a Diversity & Inclusion (D&I) Action Plan. This service will be available for anyone interested in working with or for an organisation committed to creating diverse and inclusive working environments.

Features to be included are:
* Search functionality
* User account system

Additional information can be found in the project wiki: https://stgit.dcs.gla.ac.uk/tp3-2020-CS32/cs32-main/-/wikis/home

## Installation

Can be accessed externally through the following URL: https://2401566a.pythonanywhere.com/

For development, the following packages are required by running the following command `pip install -r requirements.txt` within the virtual environment:
```asgiref==3.3.1
Django==3.1.5
Pillow==8.1.0
pytz==2020.5
sqlparse==0.4.1
```
## Populating the database
You can both populate an empty databse, and export population data from your current database

**Importing** <br />
Assuming you have a valid json file

1. Delete your db.sqlite3 and migrations
2. Set up the database tables <br />
-- 2.a Run "manage.py makemigrations" <br />
-- 2.b Run "manage.py migrate --run-syncdb"
3. Run "manage.py loaddata dumpdata.json"

**Exporting**
1. Run "manage.py dumpdata paths {auth} {admin} > dumpdata.json" - include {} apps if you wish to export accounts too

## Contributing

Sam Walker (Customer Contact) - 2379093w@student.gla.ac.uk <br />
Sam Alsumidaie (Front end for standalone App) - 2401566a@student.gla.ac.uk <br />
Jaroslav Hudacky (Backend Django App) - 2394122h@student.gla.ac.uk <br />
Paul O'Hagan (Backend Django App) - 2393709o@student.gla.ac.uk <br />
Mert Zorlu (Front end for standalone App) - 2377215z@student.gla.ac.uk <br />
<br />
Team Coach: Vishrut Singh - 2284553S@student.gla.ac.uk <br />
