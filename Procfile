release: python manage.py migrate
web: daphne chat_room.asgi:applicatoin --port $PORT --bind 0.0.0.0 -v2