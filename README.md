# Mini example of Flask ORM with SQLAlchemy

![Actions Workflow](https://github.com/po5i/flask-mini-orm/workflows/Flask/badge.svg)

This is a example repository for [my article](https://dev.to/po5i/how-to-add-type-annotations-to-sqlalchemy-models-376g).

## Setup

Create and activate the virtual environment

```bash
virtualenv venv
source venv/bin/activate
```

Run the server

```bash
python app.py
```

Run the static type check

```bash
mypy app.py
```

The server will be up on [http://localhost:5000](http://localhost:5000) and a database file named `db.sqlite3` is created.

## How it works

The toy API has four endpoints:

Endpoint | Description
-- | --
`GET /` | Returns hello world
`GET /notifications` | Returns all notifications
`POST /notifications` | Adds a notification on the DB
`GET /notifications/unread` | Returns all unread notifications

If you want to add a notification on the DB, you can use this cURL command:

```bash
curl -X POST \
  'http://localhost:5000/notifications' \
  --header 'Accept: */*' \
  --form 'description="Foo"' \
  --form 'date="2022-03-20T18:09:22"' \
  --form 'url="http://foo.bar.com"' \
  --form 'email="foo@bar.com"'
```

## Requirements

Python >= 3.9

## License

[MIT](http://www.opensource.org/licenses/mit-license.html)
