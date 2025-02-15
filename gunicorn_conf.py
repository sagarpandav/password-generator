import os

workers = int(os.environ.get('GUNICORN_PROCESSES', '5'))
# threads = int(os.environ.get('GUNICORN_THREADS', '4'))
timeout = int(os.environ.get('GUNICORN_TIMEOUT', '10'))
bind = os.environ.get('GUNICORN_BIND', '0.0.0.0:8000')

accesslog = '-'  # Logs to stdout
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(M)s"'
errorlog = '-'   # Logs to stderr
