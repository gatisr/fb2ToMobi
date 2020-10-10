# convert FB2 to MOBI 

First python project for language learning purposes

Plan is to develop **Django REST API** which **converts FB2** (open XML-based e-book format) **to MOBI** (KINDLE e-book format) 

In order to run project:

```bash
    pip install -r requirements.txt
    cd .\fb2tomobi\
    python manage.py migrate --run-syncdb
    python manage.py runserver
```

http://localhost:8000/
http://localhost:8000/admin

```bash
    Login: gatis_riders
    Pass: admin
```
