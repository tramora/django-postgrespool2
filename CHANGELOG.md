# Changelog
All notable changes to this project will be documented in this file.

## 0.2.0 - 2018-02-13
### Added
- Now you can specify backend for engine. Example:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django_postgrespool2.psycopg2',
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': 'test',
        'PASSWORD': 'test',
    }
}
```
 Available backends: **django_postgrespool2.psycopg2**, **django_postgrespool2.postgis**. By default it using psycopg2 as backend engine.
### Changed
- Update to Django 2.0
- Fix error with pre_ping option
- Fix error with __version__

## 0.1.0 - 2017-09-14
- Initial release
