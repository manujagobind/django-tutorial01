# Learning Django

## Useful commands

### Create a project

```
django-admin startproject <project-name>
```

### Start the development server

```
python manage.py runserver
```

### Create an app

```
python manage.py startapp <app-name>
```

### Create migrations

```
python manage.py makemigrations <app-name>
```

### Run migrations

```
python manage.py migrate
```

## Notes

- An app can live anywhere on the Python path. An app can be used in multiple projects.
- Need to revisit model relationships.
- In templates, use app_name:view_name instead of hardcoding urls. This decouples templates from url definitions and changing urls only requires a change in urls.py.