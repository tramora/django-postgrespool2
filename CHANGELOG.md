# Changelog
All notable changes to this project will be documented in this file.
## 2.0.0 - 2021-02-28
### Added
- Support django 2.2, 3.0 and 3.1
- Support python 3.6, 3.7, 3.8 and 3.9
### Removed
- Remove support django 1.8, 1.9, 2.0, 2.1
- Remove support python 3.4 and 3.5

## 1.0.1 - 2020-03-15
### Fixed
- Fixed installation on python 3.7, thanks [chickahoona](https://github.com/lcd1232/django-postgrespool2/pull/16)

## 1.0.0 - 2019-09-09
### Added
- New setting `DATABASE_POOL_CLASS`, thanks [mozartilize](https://github.com/mozartilize)
## Changed
- Rewrite internal logic of library, thanks [mozartilize](https://github.com/mozartilize)
### Removed
- Remove support python 3.3
- Remove support django 1.7
### Fixed
- Add missed backend `django_postgrespool2.postgis`

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
