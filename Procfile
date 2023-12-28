release: python manage.py makemigrations && python manage.py migrate
web: daphne chat_room.asgi:application --port $PORT --bind 0.0.0.0 -v2
chatworker: python manage.py runworker --settings=chat_room.settings -v2