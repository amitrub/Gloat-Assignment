# Gloat-Assignment

The Srever is writen in Python useing Django web framework

## Quick Start

- clone the git project to your local device:

```
git clone https://github.com/amitrub/Gloat-Assignment.git
```

- enter to the main app dir.

```
cd to $MAIN_DIR/Gloat-Assignment/matcher
```

### With Docker and MySql

- you need to have on your device installed - docker.
- run the app by docker compose:

```
docker compose up
```

### With Local and Sqlite

- you need to have on your device installed - python, pip, and if you are using MySql you need to install it too.
- to setup app configuration run:
```
./setup
```
- after setup if you want to run the app again run:
```
python manage.py runserver
```
