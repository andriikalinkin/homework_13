# homework_13.1

---
## How to launch the project

1. Install dependencies
    ```
    pip install -r requirements.txt
    ```

1. Make migrations
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

1. U can use Django custom command to fill the DB with some posts
    ```
    python manage.py generate_posts 10
    ```

1. Install Docker. Download "Redis" official, and run it in 1-st terminal window
    ```
    docker run -p 6379:6379 --name redis --rm redis
    ```

1. Run Django server in 2-nd terminal window
   ```
   python manage.py runserver
   ```

1. Go to
http://127.0.0.1:8000/blog/ or
http://127.0.0.1:8000/blog/1
