test:
	`which django-admin.py` test --settings=pyas2.test_settings --pythonpath=.

run:
	`which django-admin.py` runas2server --settings=pyas2.test_settings --pythonpath=.

makemigrations:
	`which django-admin.py` makemigrations pyas2 --settings=pyas2.test_settings --pythonpath=.
