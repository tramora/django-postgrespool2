![PyPI - Django Version](https://img.shields.io/pypi/djversions/django-postgrespool2)
[![PyPI - License](https://img.shields.io/pypi/l/django-postgrespool2)](https://github.com/lcd1232/django-postgrespool2/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/django-postgrespool2)](https://pypi.org/project/django-postgrespool2/)

# Django-PostgresPool2
This is simple PostgreSQL connection pooling for Django. You can use it as an alternative for [PgBouncer](https://www.pgbouncer.org/).
This is a fork of the original [django-postgrespool](https://github.com/kennethreitz/django-postgrespool).

## Installation

Installing Django-PostgresPool2 is simple, with pip:
```bash
$ pip install django-postgrespool2
```

## Usage

Using Django-PostgresPool2 is simple, just set `django_postgrespool2` as your connection engine:
```python
DATABASES = {
    "default": {
        "ENGINE": "django_postgrespool2",
        "NAME": "yourdb",
        "USER": "user",
        "PASSWORD": "some_password",
        "HOST": "localhost",
    }
}
```
If you're using the [environ](https://github.com/joke2k/django-environ) module:
```python
import environ

env = environ.Env()

DATABASES = {"default": env.db("DATABASE_URL", engine="django_postgrespool2")}
```
Everything should work as expected.

Configuration
-------------

Optionally, you can provide pool class to construct the pool (default `sqlalchemy.pool.QueuePool`) or additional options to pass to SQLAlchemy's pool creation.
List of possible values `DATABASE_POOL_CLASS` is [here](https://docs.sqlalchemy.org/en/14/core/pooling.html#api-documentation-available-pool-implementations)
```python
DATABASE_POOL_CLASS = 'sqlalchemy.pool.QueuePool'

DATABASE_POOL_ARGS = {
    'max_overflow': 10,
    'pool_size': 5,
    'recycle': 300,
}
```
Here's a basic explanation of two of these options:

-   **pool_size** – The *minimum* number of connections to maintain in the pool.
-   **max_overflow** – The maximum *overflow* size of the pool. This is not the maximum size of the pool.
-   **recycle** - Number of seconds between connection recycling, which means upon checkout, if this timeout is surpassed the connection will be closed and replaced with a newly opened connection.

The total number of "sleeping" connections the pool will allow is `pool_size`. The total simultaneous connections the pool will allow is `pool_size + max_overflow`.

As an example, databases in the [Heroku Postgres](https://www.heroku.com/postgres) starter tier have a maximum connection limit of 20. In that case your `pool_size` and `max_overflow`, when combined, should not exceed 20.

Check out the official [SQLAlchemy Connection Pooling](http://docs.sqlalchemy.org/en/latest/core/pooling.html#sqlalchemy.pool.QueuePool.__init__) docs to learn more about the optoins that can be defined in `DATABASE_POOL_ARGS`.
