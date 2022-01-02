python manage.py makemigrations esp
python manage.py migrate --no-input
# pip freeze > requirements.txt

exec "$@"