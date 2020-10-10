# convert FB2 to MOBI

 **Django REST API** which **converts FB2** (open XML-based e-book format) **to MOBI** (KINDLE e-book format)

In order to run project download calibre: https://calibre-ebook.com/download_portable
edit `.\fb2tomobi\fb2tomobi\settings.py` constant `CALIBRE_CONVERTER_LOCATION` to calibre ebook-convert.exe location (tested only on windows)

```bash
    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate --run-syncdb
    python manage.py runserver
```

api url: http://localhost:8000/
admin api url: http://localhost:8000/admin

admin acc creation:

```bash
    python manage.py createsuperuser
```
