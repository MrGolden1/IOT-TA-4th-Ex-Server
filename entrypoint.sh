python manage.py makemigrations
python manage.py migrate --no-input
# pip freeze > requirements.txt

exec "$@"