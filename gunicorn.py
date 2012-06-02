"""gunicorn WSGI server configuration."""


from multiprocessing import cpu_count
from os import environ


def max_workers():
    return cpu_count() * 2 + 1


bind = '0.0.0.0:' + environ.get('PORT', '8000')
workers = max_workers()
