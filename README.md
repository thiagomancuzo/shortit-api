# sort.it

It's an url shortener tool, composed by 3 applications:

1. shortit-api (this project)
2. shortit-management (coming soon)
3. shortit-redirector (coming soon)

This project is currently under contruction. Updates will directly reflect on this documentation!

## Quick Start

Environment variables:

```
SHORTIT_SECRET="something-really-secret"
```

and for dev time:

```
FLASK_APP="/path/to/app.py"
FLASK_DEBUG=1
```

bootstrap db

```
flask db init
flask db migrate
flask db upgrade
```

and finally, running

```
flask run
```

See you =D