coverage run --source='.' manage.py test
coverage report --omit='conf.py','bet1929/__init__.py','bet1929/wsgi.py'
